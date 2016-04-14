class Registers(object):
    def __init__(self):
        self._reg = bytearray(8)

    def __getitem__(self, item):
        try:
            assert item >= 0
            return self._reg[item]
        except (AssertionError, IndexError):
            return None

    def __setitem__(self, item, value):
        try:
            assert item >= 0
            self._reg[item] = value
            return True
        except (AssertionError, IndexError):
            return None

    def print(self):
        print('Registers')
        for i, v in enumerate(self._reg):
            print('{}: {}'.format(i, v))


if __name__ == '__main__':
    r = Registers()
    r[9] = 3
    r[4] += 200
    r.print()
