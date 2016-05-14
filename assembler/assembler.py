#!/usr/bin/python3.5

import os
import re
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from opcodes import OPCODES


class Assembler(object):
    token_pattern = r"""
                   \[.*\]|      # for DB
                   %.*|         # for directives
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
        """Method is used to read the file
        """
        with open(fname) as f:
            self.code = f.read()

    def remove_comments(self):
        """Method removes all comments
        """
        self.code = re.sub(self.comment_pattern, '\n', self.code)

    def parse_db(self):
        """Method wraps bytes after DB in square brackets
        """
        self.code = re.sub(self.db_pattern, 'DB [\\1]\n', self.code)

    def filter_tokens(self):
        """Method changes code from str to list of tokens
        """
        self.code = re.findall(self.token_pattern, self.code, re.VERBOSE)

    def parse_directives(self):
        """Method searches directives and adds values from %define to opcodes
        """
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

    def expand_db(self):
        """Method removes 'DB' tokens and adds bytes to the code
        """
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

    def expand_labels(self):
        """Method removes labels and adds their addresses to opcodes
        """
        for i, v in enumerate(self.code):
            if v.endswith(':'):
                self.opcodes[v[:-1]] = self.code.index(v)
                self.code.remove(v)

    def expand_int(self):
        """Method tries to change every token to int
        """
        for i, v in enumerate(self.code):
            try:
                self.code[i] = int(v)
            except ValueError:
                pass

    def expand_quotes(self):
        """Method changes values in single quotes to their ascii number
        """
        for i, v in enumerate(self.code):
            if type(v) != int and re.match(r"'.*'", v):
                self.code[i] = ord(v[1])

    def insert_opcode(self):
        """Method changes tokens to values from opcodes
        """
        for i, v in enumerate(self.code):
            if v in self.opcodes:
                self.code[i] = self.opcodes[v]

    def parse(self, fname):
        """Method combines all necessary methods
        """
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
        """Function extracts nested list into outer list
        """
        outlist = []
        for item in inlist:
            if isinstance(item, list):
                for item2 in item:
                    outlist.append(item2)
            else:
                outlist.append(item)
        return outlist
