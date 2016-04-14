class Instructions:
    def __init__(self):
        self.ip = 0
        self.instruction_list = []

    def read_from_file(self):
        pass

    def get(self, index):
        self.ip = index
        return self.instruction_list[index]

    def pop(self):
        self.ip += 1
        return self.ip - 1

    def set(self):
        pass


if __name__ == '__main__':
    foo = Instructions()
    foo.instruction_list = [1, 1, 2, 1, 2, 3]
