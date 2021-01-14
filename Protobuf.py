from enum import Enum, EnumMeta
from protobuf.pb_parser import parse
from protobuf.Structure import Structure
from protobuf.typed import get_type, TYPES


def _create_class_with_structure(message):
    attributes = {'__descriptor__': message}

    for enum in message.enums:
        d = {}
        for prop in enum.properties:
            d[prop.name] = int(prop.value)
        attributes[enum.name] = Enum(enum.name, d)
        TYPES[enum.name] = attributes[enum.name]

    for cl in message.classes:
        attributes[cl.name] = _create_class_with_structure(cl)
        TYPES[cl.name] = attributes[cl.name]

    for pr in message.properties:
        attributes[pr.name] = get_type(pr.type)
        if pr.default is not None:
            try:
                if isinstance(attributes[pr.name].ty, EnumMeta):
                    pr.default = attributes[attributes[pr.name].ty.__name__].__dict__['_member_map_'][pr.default]
                else:
                    pr.default = attributes[pr.name].ty(pr.default)
            except Exception:
                raise SyntaxError(f"wrong {pr.name}'s default value")

    result = type(message.name, (Structure,), attributes)
    return result


def create(filename):
    a = parse(filename)  # TODO: не забыть вернуть на место
    return _create_class_with_structure(a)
