import subprocess

from cpu import CPU


def main():
    cpu = CPU()

    fname = 'fib'
    if subprocess.call(['nasm', fname + '.nasm']):
        return

    cpu.instr.read_from_file(fname)

    cpu.run()


if __name__ == '__main__':
    main()