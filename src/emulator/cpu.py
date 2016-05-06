from instructions import Instructions
from memory import Memory
from registers import Registers
from stack import Stack


class CPU(object):
    def __init__(self):
        self.mem = Memory()
        self.reg = Registers()
        self.instr = Instructions(self)
        self.stack = Stack(self)
        self.zf = False
        self.cf = False

    def run(self):
        while self.instr.next():
            pass


if __name__ == '__main__':
    cpu = CPU()
    cpu.instr.read_from_file('test27')

    cpu.run()

    cpu.reg.print()
    # cpu.mem.print()
