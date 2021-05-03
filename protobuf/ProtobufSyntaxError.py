class ProtobufSyntaxError(SyntaxError):
    def __init__(self, text):
        super().__init__(text)
