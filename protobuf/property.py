class Property:
    def __init__(self, name, value, default=None, type=None, priority=None, wire_type=0):
        self.name = name
        self.value = value
        self.default = default
        self.type = type
        self.priority = priority
        self.wire_type = wire_type
