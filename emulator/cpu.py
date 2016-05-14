from instructions import Instructions
from memory import Memory
from registers import Registers
from stack import Stack


class CPU(object):
    def __init__(self, verb=0):
        self.mem = Memory()
        self.reg = Registers()
        self.instr = Instructions(self)
        self.stack = Stack(self)
        self.zf = False
        self.cf = False
        self.verb = verb

    def run(self):
        while self.instr.next(self.verb):
            pass
