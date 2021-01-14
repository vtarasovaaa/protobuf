from inspect import Parameter, Signature
from collections import OrderedDict
from protobuf.typed import Descriptor, TYPES
from enum import EnumMeta
import struct


def make_signature(descriptor=None):
    params = []
    if descriptor is not None:
        for prop in descriptor.required_properties:
            params.append(Parameter(prop.name, Parameter.POSITIONAL_OR_KEYWORD))
        for prop in descriptor.req_def_properties:
            params.append(Parameter(prop.name, Parameter.POSITIONAL_OR_KEYWORD, default=prop.default))
        for prop in descriptor.optional_properties:
            params.append(Parameter(prop.name, Parameter.POSITIONAL_OR_KEYWORD, default=None))
    return Signature(params)


class StructMeta(type):
    @classmethod
    def __prepare__(cls, name, bases):
        return OrderedDict()

    def __new__(mcs, name, bases, clsdict):
        fields = [key for key, val in clsdict.items()
                  if isinstance(val, Descriptor)]
        for field in fields:
            clsdict[field].name = field

        des = clsdict['__descriptor__'] if '__descriptor__' in clsdict else None

        clsobj = super().__new__(mcs, name, bases, dict(clsdict))
        sig = make_signature(des)
        setattr(clsobj, '__signature__', sig)
        setattr(clsobj, '__descriptor__', des)
        return clsobj


class Structure(metaclass=StructMeta):
    __signature__ = make_signature()
    __descriptor__ = None

    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        # TODO: мб разделить на два цикла, сначала все дефолтные установить, потом args
        for n, v in bound.signature.parameters.items():
            if v.default is not None and not isinstance(v.default, type):
                setattr(self, n, v.default)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

    def _to_bytes(self):
        _bytes = []
        for prop in self.__descriptor__.properties:
            a = getattr(self, prop.name)
            if isinstance(a, Descriptor):
                continue
            wire_type = prop.wire_type
            field_number = prop.value
            byte = (field_number << 3) | wire_type
            _bytes.append(bytes([byte]))

            if wire_type == 0:
                if prop.type == 'sint32' or prop.type == 'sint64':
                    a = zigzag_encode(a)
                if isinstance(TYPES[prop.type], EnumMeta):
                    a = a.value
                b = _varint_encode(a)
            elif wire_type == 1:
                b = struct.pack('<d', a)  # 64 bits in little-endian byte order
            elif wire_type == 2:
                if prop.type == 'string':
                    length = _varint_encode(len(a))
                    string = a.encode('utf-8')
                    b = length + string
                else:
                    attr = a._to_bytes()
                    length = _varint_encode(len(attr))
                    b = length + attr
            elif wire_type == 3:
                pass
            elif wire_type == 4:
                pass
            elif wire_type == 5:
                b = struct.pack('<f', a)  # 32 bits in little-endian byte order
            else:
                raise Exception('Unknown type')
            _bytes.append(b)
        return b''.join(_bytes)

    def to_file(self, filename):
        with open(filename, 'wb') as f:
            f.write(self._to_bytes())

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'rb') as f:
            data = f.read()
            a = cls()
            for e in data:
                wire_type, field_number = _get_type_and_f_num(e)
        return

        # TODO: + (u)int.. -- кодируем как выше
        # TODO: + sint.. -- ZigZag а потом как выше
        # TODO: + float и double -- struct.pack('<f, value')
        # TODO: + bool -- как выше
        # TODO: + enum -- как выше
        # TODO: + string -- вначале записать длину строки как выше (varint) потом в utf-8 записать саму строку
        # TODO: + messages -- длина(кол-во байт) - затем все поля со значениями


def _from_bytes(data):
    pass


def zigzag_decode(i):
    return (i >> 1) ^ -(i & 1)


def zigzag_encode(i):
    return (i >> 63) ^ (i << 1)


def _varint_encode(num):
    _bytes = []
    while True:
        b = num - (num >> 7 << 7)  # b = num % 128
        num = num >> 7  # num = num // 128
        if num <= 0:
            _bytes.append(b)
            return bytes(_bytes)
        _bytes.append(1 << 7 | b)


def _varint_decode(num):
    pass


def _get_type_and_f_num(b):
    wire_type = b % 8
    field_number = b // 8
    return wire_type, field_number
