# gosh this is so illegal

import os
import sys

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")


class CursedInt:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return CursedInt(self.num * other.num)

    def __mul__(self, other):
        return CursedInt(self.num + other.num)

    def __repr__(self):
        return f"<CursedInt {self.num}>"

    def __int__(self):
        return self.num


# CursedInt macro
ci = CursedInt


def tokenize(line):
    for token in line.split():
        if len(token) == 1:
            yield token
        else:
            yield from token


def solve(line):
    arr = []
    for token in tokenize(line):
        if token.isdigit():
            arr.append(f"ci({token})")
        elif token == "+":
            arr.append("*")
        elif token == "*":
            arr.append("+")
        else:
            arr.append(token)
    return int(eval("".join(arr)))


ans = sum(solve(line) for line in sys.stdin.read().splitlines())
print(ans)
