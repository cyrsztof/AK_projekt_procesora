#!/usr/bin/python3.5

import sys

from cpu import CPU


def main(fname, verb=0):
    cpu = CPU(verb)

    cpu.instr.read_from_file(fname)
    cpu.run()


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Missing file name")
        sys.exit(1)
