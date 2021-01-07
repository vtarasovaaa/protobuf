class Descriptor:
    def __init__(self, name=None):
        self.name = name

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    ty = object

    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            raise TypeError(f'Expected {self.name} is {self.ty}')
        super().__set__(instance, value)


class Integer(Typed):
    ty = int


class Float(Typed):
    ty = float


class String(Typed):
    ty = str


class Bool(Typed):
    ty = bool


def get_type(ty):
    if ty == int:
        return Integer()
    if ty == float:
        return Float()
    if ty == str:
        return String()
    if ty == bool:
        return Bool()
