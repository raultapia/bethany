#!/usr/bin/env python3
import sys
import os

class Color:
    NAME=''
    PRINTABLE_NAME=''
    FOREGROUND = ''
    BACKGROUND = ''
    def __init__(self, n, f, b):
        self.NAME = n
        self.PRINTABLE_NAME = ' '*(5-len(n)) + n if n else None
        self.FOREGROUND = f
        self.BACKGROUND = b

class Option:
    NONE  = Color(None, '\x1b[0;97m', '\x1b[1;97m')
    BUG   = Color('BUG', '\x1b[0;31m', '\x1b[1;30;41m')
    FIXME = Color('FIXME', '\x1b[0;33m', '\x1b[1;30;43m')
    HACK  = Color('HACK', '\x1b[0;35m', '\x1b[1;30;45m')
    NOTE  = Color('NOTE', '\x1b[0;36m', '\x1b[1;30;46m')
    TODO  = Color('TODO', '\x1b[0;32m', '\x1b[1;30;42m')

def awesome_print(string, line, option):
    if(option == Option.NONE):
        s = f'{option.BACKGROUND}{string}\x1b[0m'
    else:
        s = f'{option.BACKGROUND}   {option.PRINTABLE_NAME} {option.FOREGROUND} [Line {line}] {string}\x1b[0m'
    print(s)
    return len(s)

def analyze(filename):
    ret = {"BUG": 0, "FIXME": 0, "HACK": 0, "NOTE": 0, "TODO": 0}
    options = [Option.BUG, Option.FIXME, Option.HACK, Option.NOTE, Option.TODO]
    cnt = 0
    maxl = awesome_print(f'File: {filename}', None, Option.NONE)
    with open(filename) as f:
        for line in f:
            cnt += 1
            for option in options:
                x = line.find(option.NAME)
                if x >= 0:
                    line = line[x+len(option.NAME):-1]
                    line = line[1:] if line[0] == ':' else line
                    line = line.rstrip().lstrip()
                    maxl = max(maxl, awesome_print(line, cnt, option))
                    ret[option.NAME] += 1
    awesome_print("-"*(maxl-20), None, Option.NONE)
    return ret

def main():
    ok = False
    for i in range(1, len(sys.argv)):
        if not os.path.isfile(sys.argv[i]):
            raise FileNotFoundError(f"File {sys.argv[i]} does not exists")
        else:
            analyze(sys.argv[i])
            ok = True
    if not ok:
        raise ValueError("Not valid file(s) provided")

if __name__ == "__main__":
    main()
