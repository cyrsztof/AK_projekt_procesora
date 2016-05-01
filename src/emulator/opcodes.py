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


def add(system, args):
    system.reg[args[1]] += system.reg[args[0]]


def sub(system, args):
    system.reg[args[1]] -= system.reg[args[0]]


def mul(system, args):
    res = system.reg[args[0]] * system.reg[args[1]]
    system.reg[args[1]] = res & 0xff
    system.reg[args[0]] = res >> 8


def div(system, args):
    system.reg[args[1]] = system.reg[args[0]] // system.reg[args[1]]


def mod(system, args):
    system.reg[args[1]] = system.reg[args[0]] % system.reg[args[1]]


def inc(system, args):
    system.reg[args[0]] += 1


def dec(system, args):
    system.reg[args[0]] -= 1


opcodes = {
    0x00: Opcode(name='MOV', value=0x00, argc=2, execute=mov),
    0x01: Opcode(name='SET', value=0x01, argc=2, execute=set),
    0x02: Opcode(name='LD', value=0x02, argc=2, execute=load),
    0x03: Opcode(name='ST', value=0x03, argc=2, execute=store),

    0x10: Opcode(name='ADD', value=0x10, argc=2, execute=add),
    0x11: Opcode(name='SUB', value=0x11, argc=2, execute=sub),
    0x12: Opcode(name='MUL', value=0x12, argc=2, execute=mul),
    0x13: Opcode(name='DIV', value=0x13, argc=2, execute=div),
    0x14: Opcode(name='MOD', value=0x14, argc=2, execute=mod),
    0x15: Opcode(name='INC', value=0x15, argc=1, execute=inc),
    0x16: Opcode(name='DEC', value=0x16, argc=1, execute=dec),
}
