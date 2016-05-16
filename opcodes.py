import sys


class Opcode(object):
    def __init__(self, execute, argc):
        self._execute = execute
        self.name = execute.__name__
        self.argc = argc
        self.value = None
        self.arguments = []

    def parse(self, args):
        self.arguments = args

    def execute(self, system, args):
        self._execute(system, args)

    # def parse(self, instruction_list):
    #     arguments = []
    #     for arg in range(self.argc):
    #         arguments.append(instruction_list.pop())
    #     self.arguments = arguments

    def __str__(self):
        return ' '.join((self.name, *map(str, self.arguments)))


def MOV(system, args):
    system.reg[args[1]] = system.reg[args[0]]


def SET(system, args):
    system.reg[args[1]] = args[0]


def LD(system, args):
    system.reg[args[1]] = system.mem.load(system.reg[args[0]])


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
    system.reg[args[1]] //= system.reg[args[0]]


def MOD(system, args):
    system.reg[args[1]] %= system.reg[args[0]]


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


def JC(system, args):
    if system.cf:
        system.instr.ip += args[0]


def JNC(system, args):
    if not system.cf:
        system.instr.ip += args[0]


def JZ(system, args):
    if system.zf:
        system.instr.ip = args[0]


def JNZ(system, args):
    if not system.zf:
        system.instr.ip = args[0]


def JA(system, args):
    if system.cf:
        system.instr.ip = args[0]


def JNA(system, args):
    if not system.cf:
        system.instr.ip = args[0]


def JB(system, args):
    if not system.zf and not system.cf:
        system.instr.ip = args[0]


def JNB(system, args):
    if system.zf or system.cf:
        system.instr.ip = args[0]


def JE(system, args):
    if system.zf:
        system.instr.ip = args[0]


def JNE(system, args):
    if not system.zf:
        system.instr.ip = args[0]


def JMP(system, args):
    system.instr.ip = args[0]


def PUSH(system, args):
    system.stack.push(system.reg[args[0]])


def POP(system, args):
    system.reg[args[0]] = system.stack.pop()


def CALL(system, args):
    system.stack.push(system.instr.ip)
    system.instr.ip = args[0]


def RET(system, args):
    system.instr.ip = system.stack.pop()


def OUT(system, args):
    print(chr(system.reg[args[0]]), end='')


def END(system, args):
    sys.exit(0)


OPCODES = {
    0x00: Opcode(execute=MOV, argc=2),
    0x01: Opcode(execute=SET, argc=2),
    0x02: Opcode(execute=LD, argc=2),
    0x03: Opcode(execute=ST, argc=2),

    0x10: Opcode(execute=ADD, argc=2),
    0x11: Opcode(execute=SUB, argc=2),
    0x12: Opcode(execute=MUL, argc=2),
    0x13: Opcode(execute=DIV, argc=2),
    0x14: Opcode(execute=MOD, argc=2),
    0x15: Opcode(execute=INC, argc=1),
    0x16: Opcode(execute=DEC, argc=1),

    0x20: Opcode(execute=OR, argc=2),
    0x21: Opcode(execute=AND, argc=2),
    0x22: Opcode(execute=XOR, argc=2),
    0x23: Opcode(execute=NOT, argc=1),
    0x24: Opcode(execute=SHR, argc=2),
    0x25: Opcode(execute=SHL, argc=2),

    0x30: Opcode(execute=CMP, argc=2),
    0x31: Opcode(execute=JC, argc=1),
    0x32: Opcode(execute=JNC, argc=1),
    0x33: Opcode(execute=JZ, argc=1),
    0x34: Opcode(execute=JNZ, argc=1),
    0x35: Opcode(execute=JA, argc=1),
    0x36: Opcode(execute=JNA, argc=1),
    0x37: Opcode(execute=JB, argc=1),
    0x38: Opcode(execute=JNB, argc=1),
    0x39: Opcode(execute=JE, argc=1),
    0x3a: Opcode(execute=JNE, argc=1),
    0x3b: Opcode(execute=JMP, argc=1),

    0x40: Opcode(execute=PUSH, argc=1),
    0x41: Opcode(execute=POP, argc=1),

    0x50: Opcode(execute=CALL, argc=1),
    0x51: Opcode(execute=RET, argc=0),

    0xf0: Opcode(execute=OUT, argc=1),
    0xff: Opcode(execute=END, argc=0),
}

for i in OPCODES:
    OPCODES[i].value = i
