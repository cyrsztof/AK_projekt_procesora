class Registers(object):
    def __init__(self):
        self._reg = bytearray(8)

    def __getitem__(self, item):
        assert item in range(len(self._reg)), 'there is only %s registers' % len(self._reg)

        return self._reg[item]

    def __setitem__(self, item, value):
        assert item in range(len(self._reg)), 'there is only %s registers' % len(self._reg)
        assert value in range(256), 'byte must be in range(256)'

        self._reg[item] = value

    def print(self):
        print('Registers')
        for i, v in enumerate(self._reg):
            print('{}: {}'.format(i, v))


if __name__ == '__main__':
    r = Registers()
    r[1] = 3
    r[4] += 200
    r.print()
