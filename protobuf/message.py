class Message:
    def __init__(self, name, parent, is_enum=False):
        self.name = name
        self.properties = []
        self.is_enum = is_enum
        self.classes = []
        self.enums = []
        self.parent = parent
