from protobuf.message import Message
from protobuf.property import Property
from protobuf.typed import TYPES, WIRE_TYPES

# TODO: в целом почистить надо код
# TODO: добавить обработку первой строки с синтаксисом
PRIORITIES = {
    'required',
    'optional',
    'repeated'
}


def _read_file(filename):
    with open(filename) as f:
        code = f.read()
    return code


def parse(filename):
    code = _read_file(filename)
    lines = []
    start = 0
    for i in range(len(code)):
        if code[i] == '{' or code[i] == '}' or code[i] == ';':
            lines.append(code[start:i + 1].strip())
            start = i + 1

    message = None
    for line in lines:
        if line[-1] == '{':
            string = line[:-1].split()
            if len(string) != 2:
                raise SyntaxError(f'unexpected string: {line}')
            if string[0] == 'message':
                if message is None:
                    message = Message(line.split()[1], None)
                else:
                    message.classes.append(Message(line.split()[1], message))
                    message = message.classes[-1]
                TYPES[message.name] = type(message.name, (), {})
                WIRE_TYPES[message.name] = 2
            elif string[0] == 'enum':
                if message is None:
                    message = Message(line.split()[1], None, True)
                else:
                    message.enums.append(
                        Message(line.split()[1], message, True))
                    message = message.enums[-1]
                TYPES[message.name] = type(message.name, (), {})
                WIRE_TYPES[message.name] = 0
            else:
                raise SyntaxError(f'unexpected string: {line}')
        if line[-1] == ';':
            line = line[:-1]
            default = line.split('default')
            if len(default) < 2:
                default = None
            elif len(default) == 2:
                if len(default[0].split('[')) != 2:
                    raise SyntaxError(f'Incorrect string {line}')
                if len(default[1].split(']')) != 2:
                    raise SyntaxError(f'Incorrect string {line}')
                default = line.split('[')[1].split('=')[1].split(']')[0].strip()  # TODO: для строк сплитить по кавычкам
                line = line.split('[')[0]
            else:
                raise SyntaxError(f'Incorrect string {line}')
            w = line.split('=')
            if len(w) != 2:
                raise SyntaxError(f'Incorrect string {line}')
            line = ' '.join([w[0], w[1]])
            words = line.split()
            if not message.is_enum:
                if len(words) != 4:
                    raise SyntaxError(f'unexpected string: {line}')
                if words[1] not in TYPES:
                    raise SyntaxError(f'unexpected string: {line}')
                if words[0] not in PRIORITIES:
                    raise SyntaxError(f'unexpected string: {line}')

                prop = Property(
                    words[2], int(words[3]), default, words[1], words[0], WIRE_TYPES[words[1]])
            else:
                if len(words) != 2:
                    raise SyntaxError(f'unexpected string: {line}')
                prop = Property(words[0], words[1])

            if prop.priority == 'optional':
                message.optional_properties.append(prop)
            elif prop.priority == 'required':
                if prop.default is None:
                    message.required_properties.append(prop)
                else:
                    message.req_def_properties.append(prop)
            message.properties.append(prop)

        if line[-1] == '}':
            if message.parent is not None:
                message = message.parent

    return message
