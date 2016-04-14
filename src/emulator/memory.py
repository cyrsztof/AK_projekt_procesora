class Memory(object):
    def __init__(self):
        self._mem = bytearray(256)

    def load(self, address):
        try:
            assert address >= 0
            return self._mem[address]
        except (AssertionError, IndexError):
            return None

    def store(self, address, value):
        try:
            assert address >= 0
            self._mem[address] = value
            return True
        except (AssertionError, IndexError):
            return None

    def print(self):
        print('Memory:')
        for i, v in enumerate(self._mem):
            print('{}: {}'.format(i, v))


if __name__ == '__main__':
    m = Memory()
    print(m.store(209, 44))
    print(m.load(343))
    m.print()
