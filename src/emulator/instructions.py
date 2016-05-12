from opcodes import opcodes


class Instructions(object):
    def __init__(self, cpu):
        self.cpu = cpu
        self.mem = cpu.mem
        self.reg = cpu.reg
        self.ip = 0

    def read_from_file(self, fname):
        with open(fname, 'rb') as f:
            data = f.read()

        print('file', fname, len(data), list(data))
        self.store_in_memory(data)

    def store_in_memory(self, data):
        for i, datum in enumerate(data):
            self.mem.store(i, datum)

    def get(self, index):
        self.ip = index
        return self.mem[index]

    def next(self):
        opcode = opcodes[self.mem.load(self.pop())]
        argv = [self.mem.load(self.pop()) for _ in range(opcode.argc)]

        if opcode.value == 0 and argv == [0, 0]:
            return False

        opcode.parse(argv)
        opcode.execute(self.cpu, argv)

        self.debug(opcode, 0)

        return True

    def debug(self, opcode, verb=0):
        if verb > 0:
            print('\t{:<6}{}'.format(self.ip, opcode))
            if verb > 1:
                print('z, c = {:d}, {:d}'.format(self.cpu.zf, self.cpu.cf))
                self.reg.print()
                self.mem.print()

    def pop(self):
        self.ip += 1
        return self.ip - 1

    def set(self):
        pass
