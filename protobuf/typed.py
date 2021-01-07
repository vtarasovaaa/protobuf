TYPES = {
    'double': float,
    'float': float,
    'int': int,
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
    'string': str,
    'str': str
}


class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    ty = object

    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError(f'Expected {self.name} is {self.ty} but was {type(value)}')
        super().__set__(instance, value)


def get_type(ty):
    return type(ty.__name__, (Typed, ), {'ty': TYPES[ty.__name__]})()
