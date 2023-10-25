#!/usr/bin/env python3
import os
import argparse


class Color:
    def __init__(self, n, f, b):
        self.NAME = n
        self.PRINTABLE_NAME = " " * (5 - len(n)) + n if n else None
        self.FOREGROUND = f
        self.BACKGROUND = b


class Option:
    NONE = Color(None, "\x1b[0;97m", "\x1b[1;97m")
    BUG = Color("BUG", "\x1b[0;31m", "\x1b[1;30;41m")
    FIXME = Color("FIXME", "\x1b[0;33m", "\x1b[1;30;43m")
    HACK = Color("HACK", "\x1b[0;35m", "\x1b[1;30;45m")
    NOTE = Color("NOTE", "\x1b[0;36m", "\x1b[1;30;46m")
    TODO = Color("TODO", "\x1b[0;32m", "\x1b[1;30;42m")


def awesome_print(string, line, option, filename=""):
    if option == Option.NONE:
        s = f"{option.BACKGROUND}{string}\x1b[0m"
    else:
        if filename:
            s = f"{option.BACKGROUND}   {option.PRINTABLE_NAME} {option.FOREGROUND} {string} [Line {line} @ {filename}]\x1b[0m"
        else:
            s = f"{option.BACKGROUND}   {option.PRINTABLE_NAME} {option.FOREGROUND} [Line {line}] {string}\x1b[0m"
    print(s)
    return len(s)


def analyze(filename, continuous=False):
    ret = {"BUG": 0, "FIXME": 0, "HACK": 0, "NOTE": 0, "TODO": 0}
    options = [Option.BUG, Option.FIXME, Option.HACK, Option.NOTE, Option.TODO]
    cnt = 0
    maxl = 0
    if not continuous:
        maxl = awesome_print(f"File: {filename}", None, Option.NONE)
    with open(filename) as f:
        for line in f:
            cnt += 1
            for option in options:
                x = line.find(option.NAME + ":")
                if x >= 0:
                    line = line[x + len(option.NAME):-1]
                    if len(line) > 0:
                        line = line[1:] if line[0] == ":" else line
                        line = line.rstrip().lstrip()
                    else:
                        line = "<NO MESSAGE>"
                    n = awesome_print(line, cnt, option, filename * continuous)
                    maxl = max(maxl, n)
                    ret[option.NAME] += 1
    if not continuous:
        awesome_print("-" * (maxl - 20), None, Option.NONE)
    return ret


def main():
    parser = argparse.ArgumentParser(
        description="A command line tool to list all BUG, TODO, HACK, NOTE, and FIXME keywords in your code.")
    parser.add_argument("files", nargs="+", help="files to analyze")
    parser.add_argument("-c", "--continuous",
                        action="store_true",
                        help="enable continuous mode")
    args = parser.parse_args()

    ok = False
    for i in range(len(args.files)):
        if not os.path.isfile(args.files[i]):
            raise FileNotFoundError(f"File {args.files[i]} does not exist")
        else:
            analyze(args.files[i], args.continuous)
            ok = True
    if not ok:
        raise ValueError("Not valid file(s) provided")


if __name__ == "__main__":
    main()
