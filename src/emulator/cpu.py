from instructions import Instructions
from memory import Memory
from registers import Registers


class CPU(object):
    def __init__(self):
        self.mem = Memory()
        self.reg = Registers()
        self.instr = Instructions(self)
        self.zf = False
        self.cf = False

    def run(self):
        while self.instr.next():
            print('zf', self.zf)
            print('cf', self.cf)


if __name__ == '__main__':
    cpu = CPU()
    cpu.instr.read_from_file('test25')

    cpu.run()

    cpu.reg.print()
    # cpu.mem.print()
