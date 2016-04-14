from memory import Memory
from registers import Registers


class CPU(object):
    def __init__(self):
        self._mem = Memory()
        self._reg = Registers()


if __name__ == '__main__':
    cpu = CPU()
