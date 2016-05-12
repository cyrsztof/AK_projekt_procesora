import subprocess

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

    fname = 'fib.nasm'
    subprocess.call(['nasm', fname])
    cpu.instr.read_from_file(fname.split('.')[0])

    cpu.run()
