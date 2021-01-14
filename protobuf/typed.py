TYPES = {
    'double': float,
    'float': float,
    'int32': int,
    'int64': int,
    'uint32': int,
    'uint64': int,
    'sint32': int,
    'sint64': int,
    'fixed32': int,
    'fixed64': int,
    'sfixed32': int,
    'sfixed64': int,
    'bool': bool,
    'string': str
}

WIRE_TYPES = {
    'double': 1,
    'float': 5,
    'int32': 0,
    'int64': 0,
    'uint32': 0,
    'uint64': 0,
    'sint32': 0,
    'sint64': 0,
    'fixed32': 5,
    'fixed64': 1,
    'sfixed32': 5,
    'sfixed64': 1,
    'bool': 0,
    'string': 2
}


class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    ty = object

    def __set__(self, instance, value):
        if not isinstance(value, self.ty) and value is not None:  # TODO: None?
            raise TypeError(f'Expected {self.name} is {self.ty} but was {type(value)}')
        super().__set__(instance, value)


def get_type(ty):  # TODO: название
    return type(TYPES[ty].__name__, (Typed,), {'ty': TYPES[ty]})()
