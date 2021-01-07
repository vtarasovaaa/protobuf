from enum import Enum
from protobuf.pb_parser import parse
from protobuf.Structure import Structure, make_signature

CLASSES = {}


def _create_class(message):
    CLASSES[message.name] = message.properties

    def init(self, *args):
        if len(args) != len(CLASSES[type(self).__name__]):
            raise AttributeError(f'{type(self).__name__}'
                                 f' should take '
                                 f'{len(CLASSES[type(self).__name__])}'
                                 f' arguments')
        for i in range(len(args)):
            setattr(self, CLASSES[type(self).__name__][i].name, args[i])

    attributes = {'__init__': init}

    for enum in message.enums:
        d = {}
        for prop in enum.properties:
            d[prop.name] = prop.value
        attributes[enum.name] = Enum(enum.name, d)

    for mes in message.classes:
        attributes[mes.name] = _create_class(mes)

    result = type(message.name, (), attributes)
    return result


def _create_class_with_structure(message):
    attributes = {}

    for enum in message.enums:
        d = {}
        for prop in enum.properties:
            d[prop.name] = prop.value
        attributes[enum.name] = Enum(enum.name, d)

    for mes in message.classes:
        attributes[mes.name] = _create_class(mes)

    attributes['__signature__'] = make_signature(message.properties)

    result = type(message.name, (Structure, ), attributes)
    return result


def create(filename):
    return _create_class_with_structure(parse(filename))
