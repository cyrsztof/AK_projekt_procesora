import sys


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


def MOV(system, args):
    system.reg[args[1]] = system.reg[args[0]]


def SET(system, args):
    system.reg[args[1]] = args[0]


def LD(system, args):
    byte = system.mem.load(system.reg[args[0]])
    if byte is None:
        return None
    system.reg[args[1]] = byte


def ST(system, args):
    system.mem.store(system.reg[args[1]], system.reg[args[0]])


def ADD(system, args):
    system.reg[args[1]] += system.reg[args[0]]


def SUB(system, args):
    system.reg[args[1]] -= system.reg[args[0]]


def MUL(system, args):
    res = system.reg[args[0]] * system.reg[args[1]]
    system.reg[args[1]] = res & 0xff
    system.reg[args[0]] = res >> 8


def DIV(system, args):
    system.reg[args[1]] //= system.reg[args[0]]  # // system.reg[args[1]]


def MOD(system, args):
    system.reg[args[1]] %= system.reg[args[0]]  #% system.reg[args[1]]


def INC(system, args):
    system.reg[args[0]] += 1


def DEC(system, args):
    system.reg[args[0]] -= 1


def OR(system, args):
    system.reg[args[1]] |= system.reg[args[0]]


def AND(system, args):
    system.reg[args[1]] &= system.reg[args[0]]


def XOR(system, args):
    system.reg[args[1]] ^= system.reg[args[0]]


def NOT(system, args):
    system.reg[args[0]] ^= 0xff


def SHL(system, args):
    system.reg[args[1]] = (system.reg[args[1]] << system.reg[args[0]]) & 0xff


def SHR(system, args):
    system.reg[args[1]] = system.reg[args[1]] >> system.reg[args[0]]


def CMP(system, args):
    res = system.reg[args[1]] - system.reg[args[0]]
    system.zf = res == 0
    system.cf = res < 0


def JZ(system, args):
    if system.zf:
        system.instr.ip += args[0]
        system.instr.ip &= 0xff


def JNZ(system, args):
    if not system.zf:
        system.instr.ip += args[0]
        system.instr.ip &= 0xff


def JC(system, args):
    if system.cf:
        system.instr.ip += args[0]
        system.instr.ip &= 0xff


def JNC(system, args):
    if not system.cf:
        system.instr.ip += args[0]
        system.instr.ip &= 0xff


def PUSH(system, args):
    system.stack.push(system.reg[args[0]])


def POP(system, args):
    system.reg[args[0]] = system.stack.pop(args[0])


def OUT(system, args):
    print(chr(system.reg[args[0]]), end='')


def END(system, args):
    sys.exit(0)


opcodes = {
    0x00: Opcode(name='MOV', value=0x00, argc=2, execute=MOV),
    0x01: Opcode(name='SET', value=0x01, argc=2, execute=SET),
    0x02: Opcode(name='LD', value=0x02, argc=2, execute=LD),
    0x03: Opcode(name='ST', value=0x03, argc=2, execute=ST),

    0x10: Opcode(name='ADD', value=0x10, argc=2, execute=ADD),
    0x11: Opcode(name='SUB', value=0x11, argc=2, execute=SUB),
    0x12: Opcode(name='MUL', value=0x12, argc=2, execute=MUL),
    0x13: Opcode(name='DIV', value=0x13, argc=2, execute=DIV),
    0x14: Opcode(name='MOD', value=0x14, argc=2, execute=MOD),
    0x15: Opcode(name='INC', value=0x15, argc=1, execute=INC),
    0x16: Opcode(name='DEC', value=0x16, argc=1, execute=DEC),

    0x20: Opcode(name='OR', value=0x20, argc=2, execute=OR),
    0x21: Opcode(name='AND', value=0x21, argc=2, execute=AND),
    0x22: Opcode(name='XOR', value=0x22, argc=2, execute=XOR),
    0x23: Opcode(name='NOT', value=0x23, argc=1, execute=NOT),
    0x24: Opcode(name='SHL', value=0x24, argc=2, execute=SHL),
    0x25: Opcode(name='SHR', value=0x25, argc=2, execute=SHR),

    0x30: Opcode(name='CMP', value=0x30, argc=2, execute=CMP),
    0x31: Opcode(name='JZ', value=0x31, argc=1, execute=JZ),
    0x32: Opcode(name='JNZ', value=0x32, argc=1, execute=JNZ),
    0x33: Opcode(name='JC', value=0x33, argc=1, execute=JC),
    0x34: Opcode(name='JNC', value=0x34, argc=1, execute=JNC),

    0x40: Opcode(name='PUSH', value=0x40, argc=1, execute=PUSH),
    0x41: Opcode(name='POP', value=0x41, argc=1, execute=POP),

    0xf2: Opcode(name='OUT', value=0xf2, argc=1, execute=OUT),
    0xff: Opcode(name='END', value=0xff, argc=0, execute=END),
}
