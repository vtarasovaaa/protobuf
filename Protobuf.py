from enum import Enum
from protobuf.pb_parser import parse
from protobuf.Structure import Structure, make_signature


def _create_class_with_structure(message):
    attributes = {}

    for enum in message.enums:
        d = {}
        for prop in enum.properties:
            d[prop.name] = prop.value
        attributes[enum.name] = Enum(enum.name, d)

    for mes in message.classes:
        attributes[mes.name] = _create_class_with_structure(mes)

    attributes['__signature__'] = make_signature(message.properties)

    result = type(message.name, (Structure, ), attributes)
    return result


def create(filename):
    return _create_class_with_structure(parse(filename))
