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
        if len(kwargs) == 1 and '__cr__' in kwargs:
            bound = self.__signature__.bind(*args, **kwargs['__cr__'])
        else:
            bound = self.__signature__.bind(*args, **kwargs)

        for n, v in bound.signature.parameters.items():
            if v.default is not None and not isinstance(v.default, type):
                setattr(self, n, v.default)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

    def to_bytes(self):
        _bytes = []
        for prop in self.__descriptor__.properties:
            attr = getattr(self, prop.name)
            if isinstance(attr, Descriptor):
                continue

            wire_type = prop.wire_type
            field_number = prop.value
            _bytes.append(bytes([(field_number << 3) | wire_type]))
            encode_attr = 0

            if wire_type == 0:
                if prop.type == 'sint32' or prop.type == 'sint64':
                    attr = zigzag_encode(attr)
                if isinstance(TYPES[prop.type], EnumMeta):
                    attr = attr.value
                encode_attr = _varint_encode(attr)
            elif wire_type == 1:
                encode_attr = struct.pack('<d', attr)  # 64 bits in little-endian byte order
            elif wire_type == 2:
                if prop.type == 'string':
                    length = _varint_encode(len(attr))
                    string = attr.encode('utf-8')
                    encode_attr = length + string
                else:
                    attr = attr.to_bytes()
                    length = _varint_encode(len(attr))
                    encode_attr = length + attr
            elif wire_type == 3:
                pass
            elif wire_type == 4:
                pass
            elif wire_type == 5:
                encode_attr = struct.pack('<f', attr)  # 32 bits in little-endian byte order
            else:
                raise Exception('Unknown type')
            _bytes.append(encode_attr)
        return b''.join(_bytes)

    def to_file(self, filename):
        with open(filename, 'wb') as f:
            f.write(self.to_bytes())

    @classmethod
    def from_bytes(cls, data):
        properties = {}
        k = 0
        while k < len(data):
            wire_type, field_number = _get_type_and_f_num(data[k])
            prop = cls.__descriptor__.properties_dict[field_number]
            k += 1
            if wire_type == 0:
                num, k = _varint_decode(data, k)
                if prop.type == 'sint32' or prop.type == 'sint64':
                    num = zigzag_decode(num)
                if prop.type == 'bool':
                    num = bool(num)
                if isinstance(TYPES[prop.type], EnumMeta):
                    num = cls.__dict__[prop.type](num)
                properties[prop.name] = num
            elif wire_type == 1:
                num = struct.unpack('<d', data[k:k+8])
                k += 8
                properties[prop.name] = num[0]
            elif wire_type == 2:
                length, k = _varint_decode(data, k)
                if prop.type == 'string':
                    value = data[k:k + length].decode('utf-8')
                else:
                    sub_class = cls.__dict__[prop.type]
                    value = sub_class.from_bytes(data[k:k+length])
                k += length
                properties[prop.name] = value
            elif wire_type == 3:
                pass
            elif wire_type == 4:
                pass
            elif wire_type == 5:
                num = struct.unpack('<f', data[k:k+4])
                k += 4
                properties[prop.name] = num[0]
            else:
                raise Exception('Something went wrong')
        return cls(__cr__=properties)

    @classmethod
    def from_file(cls, filename):
        with open(filename, 'rb') as f:
            data = f.read()
            return cls.from_bytes(data)


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


def _varint_decode(data, k):
    result = []
    while True:
        num = data[k]
        if num < 128:
            result.append(num)
            result.reverse()
            ans = 0
            for a in result[:-1]:
                ans += a
                ans = ans << 7
            ans += result[-1]
            k += 1
            return ans, k
        result.append(num % 128)
        k += 1


def _get_type_and_f_num(b):
    return b % 8, b // 8  # wire_type, field_number
