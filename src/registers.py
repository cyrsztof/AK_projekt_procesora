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

    def clean(self):
        self._reg = bytearray(8)

    def print(self):
        print('    ' + 'Registers:')
        print('    ' + ('{:>4}' * len(self._reg)).format(*range(len(self._reg))))
        print('    ' + '-' * len(self._reg) * 4)
        print('    ' + ('{:>4}' * len(self._reg)).format(*self._reg))
