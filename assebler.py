#!/usr/bin/python3.5

import re
import sys

from opcodes import OPCODES


class Assebler(object):
    token_pattern = r""" #DB .*|       # for DB
                   \[.*\]|
                   %.*|
                   '.*'|        # for constants
                   ".*"|        # for strings
                   \w+:?        # for everything else
                   """
    comment_pattern = r';.*?\n'
    db_pattern = r'DB (.*)\n'

    def __init__(self):
        self.code = None
        self.opcodes = {v.name: k for (k, v) in OPCODES.items()}
        self.opcodes.update(dict(('R%d' % i, i) for i in range(8)))

    def read_file(self, fname):
        with open(fname) as f:
            self.code = f.read()

    def remove_comments(self):
        self.code = re.sub(self.comment_pattern, '\n', self.code)

    def parse_db(self):
        self.code = re.sub(self.db_pattern, 'DB [\\1]\n', self.code)

    def filter_tokens(self):
        self.code = re.findall(self.token_pattern, self.code, re.VERBOSE)

    def parse_directives(self):
        dirs = []
        for i, v in enumerate(self.code):
            if v.startswith('%'):
                dirs.append((i, v))

        for i, v in dirs[::-1]:
            del self.code[i]
            v = v.split()
            if v[0] == '%define':
                if v[2].startswith("'"):
                    self.opcodes[v[1]] = ord(v[2].strip("'"))
                else:
                    self.opcodes[v[1]] = int(v[2])

    def expand_labels(self):
        for i, v in enumerate(self.code):
            if v.endswith(':'):
                self.opcodes[v[:-1]] = self.code.index(v)
                self.code.remove(v)

    def expand_db(self):
        for i, v in enumerate(self.code):
            if v == 'DB':
                del self.code[i]
                item = self.code.pop(i).strip('[]').split(',')
                for ii, vv in enumerate(item):
                    vv = vv.strip()
                    if vv.startswith('"'):
                        self.code.insert(i + ii, [str(ord(j)) for j in vv.strip('"')])
                    else:
                        self.code.insert(i + ii, vv)

        self.code = self.flat_list(self.code)

    def expand_int(self):
        for i, v in enumerate(self.code):
            try:
                self.code[i] = int(v)
            except ValueError:
                pass

    def expand_quotes(self):
        for i, v in enumerate(self.code):
            if type(v) != int and re.match(r"'.*'", v):
                self.code[i] = ord(v[1])

    def insert_opcode(self):
        for i, v in enumerate(self.code):
            if v in self.opcodes:
                self.code[i] = self.opcodes[v]
                # else:
                #     print(v)

    def parse(self, fname):
        self.read_file(fname)
        self.remove_comments()
        self.parse_db()
        self.filter_tokens()
        self.parse_directives()
        self.expand_db()
        self.expand_labels()
        self.expand_int()
        self.expand_quotes()
        self.insert_opcode()
        return self.code

    @staticmethod
    def flat_list(inlist):
        outlist = []
        for item in inlist:
            if isinstance(item, list):
                for item2 in item:
                    outlist.append(item2)
            else:
                outlist.append(item)
        return outlist


def main(fname):
    a = Assebler()
    p = a.parse(fname)
    with open(fname.split('.')[0], 'wb') as f:
        f.write(bytearray(p))
        # print(p)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("Missing file name")
