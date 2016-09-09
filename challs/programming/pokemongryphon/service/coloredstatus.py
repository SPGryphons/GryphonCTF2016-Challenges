#!/usr/bin/python
# Made by Optixal

import sys
from time import sleep

caret = "\x1b[1m\x1b[38;5;88m>\x1b[38;5;125m>\x1b[1m\x1b[38;5;197m>\x1b[0m "

openlabel = "\x1b[32m[\x1b[1m\x1b[92mOPEN\x1b[0m\x1b[32m]\x1b[0m"
closelabel = "\x1b[31m[\x1b[1m\x1b[91mGONE\x1b[0m\x1b[31m]\x1b[0m"
kicklabel = "\x1b[33m[\x1b[1m\x1b[93mKICK\x1b[0m\x1b[33m]\x1b[0m"
flaglabel = "\x1b[36m[\x1b[1m\x1b[96mFLAG\x1b[0m\x1b[36m]\x1b[0m"

status = "\x1b[36m[\x1b[1m\x1b[96m\xBB\x1b[0m\x1b[36m]\x1b[0m"
good = "\x1b[32m[\x1b[1m\x1b[92m+\x1b[0m\x1b[32m]\x1b[0m"
error = "\x1b[31m[\x1b[1m\x1b[91m-\x1b[0m\x1b[31m]\x1b[0m"
warning = "\x1b[33m[\x1b[1m\x1b[93m!\x1b[0m\x1b[33m]\x1b[0m"
money = "\x1b[32m[\x1b[1m\x1b[92m$\x1b[0m\x1b[32m]\x1b[0m"
special = "\x1b[38;5;125m[\x1b[1m\x1b[38;5;197m#\x1b[0m\x1b[38;5;125m]\x1b[0m"

def greenwrap(string):
    start = "\x1b[32m[\x1b[1m\x1b[92m"
    end = "\x1b[0m\x1b[32m]\x1b[0m"
    return start + str(string) + end

def pinkwrap(string):
    start = "\x1b[38;5;125m[ \x1b[1m\x1b[38;5;197m"
    end = " \x1b[0m\x1b[38;5;125m]\x1b[0m"
    return start + str(string) + end

class fade():
    def __init__(self, start, end, char, bold=False):
        self.start = start
        self.end = end
        self.char = char
        self.bold = bold

    def fadein(self):
        decoration = "\x1b[1m" if self.bold == True else ""
        for i in range(self.start, self.end + 1):
            decoration += "\x1b[38;5;" + str(i) + "m" + self.char
        decoration += "\x1b[0m"
        return decoration

    def fadeout(self):
        decoration = "\x1b[1m" if self.bold == True else ""
        for i in range(self.end, self.start - 1, -1):
            decoration += "\x1b[38;5;" + str(i) + "m" + self.char
        decoration += "\x1b[0m"
        return decoration

    def pad(self, width):
        decoration = "\x1b[1m" if self.bold == True else ""
        decoration += "\x1b[38;5;" + str(self.end) + "m"
        decoration += self.char * width
        decoration += "\x1b[0m"
        return decoration

    def line(self, midwidth):
        decoration = self.fadein()
        decoration += self.pad(midwidth)
        decoration += self.fadeout()
        return decoration

class fade_animate():
    def __init__(self, start, end, char, mid=0, bold=False):
        self.start = start
        self.end = end
        self.char = char
        self.mid = mid
        self.bold = bold

    def line(self):

        self.specialprint("\x1b[1m" if self.bold == True else "", sleepvar=False)
        for i in range(self.start, self.end + 1):
            self.specialprint("\x1b[38;5;" + str(i) + "m" + self.char)

        for i in range(self.mid):
            self.specialprint(self.char)

        for i in range(self.end, self.start - 1, -1):
            self.specialprint("\x1b[38;5;" + str(i) + "m" + self.char)
        self.specialprint("\x1b[0m", sleepvar=False)

        print("\n")

    def specialprint(self, string, sleepvar=True):
        print(string, end="")
        sys.stdout.flush()
        if sleepvar:
            sleep(0.01)

class center_fade():
    def __init__(self, start, end, char, width, delay=0.02):
        self.start = start
        self.end = end
        self.char = char
        self.width = width + 1 if width % 2 == 0 else width
        self.delay = delay

    def build_transition(self, i):
        padding = (self.width // 2 - i // 2) * " "
        line = padding
        for j in range(0, i // 2):
            line += "\x1b[38;5;" + str(self.start + j) + "m" + self.char
        line += "\x1b[38;5;" + str(self.start + (i // 2)) + "m" + self.char
        for k in range(i // 2 - 1, -1, -1):
            line += "\x1b[38;5;" + str(self.start + k) + "m" + self.char
        line += "\x1b[0m"
        line += padding
        return line

    def animate(self):
        print()
        for i in range(1, self.width + 1, 2):
            print("\b" * self.width, end="")
            print(self.build_transition(i), end="")
            sys.stdout.flush()
            sleep(self.delay)
        print("\n")

