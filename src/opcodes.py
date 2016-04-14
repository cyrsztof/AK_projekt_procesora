class Opcode(object):
    def __init__(self, name, value, argc, execute):
        self.name = name
        self.value = value
        self.argc = argc
        self._execute = execute
        self.arguments = []

    def execute(self, system):
        self._execute(system, self.arguments)

    def parse(self, instruction_list):
        arguments = []
        for arg in range(self.argc):
            arguments.append(instruction_list.pop())
        self.arguments = arguments


def mov(system, args):
    system.register[args[2]] = system.register[args[1]]


opcodes = {
    0x00: Opcode(name='MOV', value=0x00, argc=2, execute=mov)
}
