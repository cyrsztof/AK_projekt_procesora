class Opcode(object):
    def __init__(self, name, value, argc, execute):
        self.name = name
        self.value = value
        self.argc = argc
        self._execute = execute
        self.arguments = []

    def execute(self, system, args):
        self._execute(system, args)

    def parse(self, instruction_list):
        arguments = []
        for arg in range(self.argc):
            arguments.append(instruction_list.pop())
        self.arguments = arguments


def mov(system, args):
    system.reg[args[1]] = system.reg[args[0]]


def set(system, args):
    system.reg[args[1]] = args[0]


def load(system, args):
    byte = system.mem.load(system.reg[args[0]])
    if byte is None:
        return None
    system.reg[args[1]] = byte


def store(system, args):
    system.mem.store(system.reg[args[1]], system.reg[args[0]])


opcodes = {
    0x00: Opcode(name='MOV', value=0x00, argc=2, execute=mov),
    0x01: Opcode(name='SET', value=0x01, argc=2, execute=set),
    0x02: Opcode(name='LD', value=0x02, argc=2, execute=load),
    0x03: Opcode(name='ST', value=0x03, argc=2, execute=store),
}
