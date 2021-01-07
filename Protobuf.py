from enum import Enum
from protobuf.pb_parser import parse
from protobuf.Structure import Structure
from protobuf.typed import get_type, TYPES


def _create_class_with_structure(message):
    attributes = {}

    for enum in message.enums:
        d = {}
        for prop in enum.properties:
            d[prop.name] = prop.value
        attributes[enum.name] = Enum(enum.name, d)
        TYPES[enum.name] = attributes[enum.name]

    for cl in message.classes:
        attributes[cl.name] = _create_class_with_structure(cl)
        TYPES[cl.name] = attributes[cl.name]

    for pr in message.properties:
        attributes[pr.name] = get_type(pr.type)

    result = type(message.name, (Structure, ), attributes)
    return result


def create(filename):
    a = parse(filename)
    return _create_class_with_structure(a)
