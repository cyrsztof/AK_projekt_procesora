class Stack(object):
    def __init__(self, cpu):
        self.cpu = cpu
        self.mem = cpu.mem
        self.reg = cpu.reg
        self.sp = 0xff

    def push(self, value):
        self.mem.store(self.sp, value)
        self.sp -= 1

    def pop(self, reg):
        self.sp += 1
        return self.mem.load(self.sp)
