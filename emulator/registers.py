class Registers(object):
    def __init__(self):
        self.reg = bytearray(8)

    def __getitem__(self, item):
        try:
            assert item >= 0
            return self.reg[item]
        except (AssertionError, IndexError):
            return None

    def __setitem__(self, item, value):
        try:
            assert item >= 0
            self.reg[item] = value
            return True
        except (AssertionError, IndexError):
            return None

    def clean(self):
        self.reg = bytearray(8)

    def print(self):
        print('    ' + 'Registers:')
        print('    ' + ('{:>4}' * len(self.reg)).format(*range(len(self.reg))))
        print('    ' + '-' * len(self.reg) * 4)
        print('    ' + ('{:>4}' * len(self.reg)).format(*self.reg))
