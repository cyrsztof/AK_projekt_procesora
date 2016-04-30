from instructions import Instructions
from memory import Memory
from registers import Registers


class CPU(object):
    def __init__(self):
        self.mem = Memory()
        self.reg = Registers()
        self.instr = Instructions(self)

    def run(self):
        self.instr.next()
        self.instr.next()
        self.instr.next()
        self.instr.next()
        self.instr.next()
        self.instr.next()


if __name__ == '__main__':
    cpu = CPU()
    cpu.instr.read_from_file('test5')

    cpu.run()

    print('after')
    cpu.reg.print()
    cpu.mem.print()
