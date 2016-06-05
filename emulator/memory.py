class Memory(object):
    def __init__(self):
        self.mem = bytearray(256)

    def load(self, address):
        try:
            assert address >= 0
            return self.mem[address]
        except (AssertionError, IndexError):
            return None

    def store(self, address, value):
        try:
            assert address >= 0
            self.mem[address] = value
            return True
        except (AssertionError, IndexError):
            return None

    def clean(self):
        self.mem = bytearray(256)

    def print(self):
        print('    ' + 'Memory:')
        print('    ' + ('{:>4}' * 16).format(*range(16)))
        print('    ' + '-' * 16 * 4)
        for i in range(16):
            print('{:>3}|'.format(i * 16), end='')
            for j in range(16):
                print('{:>4}'.format(self.load(i * 16 + j)), end='')
            print()
