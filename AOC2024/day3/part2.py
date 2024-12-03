import sys
import os
from pathlib import Path
import re

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")


def parse(line: str) -> list:
    pattern = r"mul\((\d+),(\d+)\)|do\(\)|don't\(\)"

    ret = []
    for match in re.finditer(pattern, line):
        if match.group() == "do()":
            ret.append("do()")
        elif match.group() == "don't()":
            ret.append("don't()")
        else:
            ret.append(match.groups())
    return ret


tokens = []
for line in sys.stdin.readlines():
    tokens.extend(parse(line))

ttl = 0
flag = True
for tok in tokens:
    if tok == "do()":
        flag = True
    elif tok == "don't()":
        flag = False
    elif flag:
        a, b = map(int, tok)
        ttl += a * b

print(ttl)
