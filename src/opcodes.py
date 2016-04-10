class Opcode(object):
    name = None
    value = None

    def execute(self):
        pass

    def encode(self, operand):
        pass

    def print(self):
        pass


class MOV(Opcode):
    name = 'MOV'
    value = 0x01
