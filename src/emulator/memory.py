class Memory(object):
    def __init__(self):
        self._mem = bytearray(256)

    def load(self, addr):
        assert addr in range(len(self._mem)), 'address must be in range(%s)' % len(self._mem)

        return self._mem[addr]

    def store(self, addr, value):
        assert addr in range(len(self._mem)), 'address must be in range(%s)' % len(self._mem)
        assert value in range(256), 'byte must be in range(256)'

        self._mem[addr] = value

    def print(self):
        print('Memory:')
        for i, v in enumerate(self._mem):
            print('{}: {}'.format(i, v))


if __name__ == '__main__':
    m = Memory()
    print(m.store(2009, 44))
    m.print()
