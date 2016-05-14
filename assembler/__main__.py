import sys

from assembler import Assembler


def main(fname):
    a = Assembler()
    p = a.parse(fname)
    with open(fname.split('.')[0], 'wb') as f:
        f.write(bytearray(p))
        # print(p)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Missing file name")
        sys.exit(1)
