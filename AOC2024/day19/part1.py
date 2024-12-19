import sys
import os
from pathlib import Path
import re
from functools import cache

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

patterns = re.findall(r"[a-z]+", input())
input()


@cache
def check(line: str, start: int) -> bool:
    global patterns

    if start == len(line):
        return True

    for p in patterns:
        if line[start:].startswith(p) and check(line, start + len(p)):
            return True
    return False


ans = 0
for line in map(lambda s: s.strip("\n"), sys.stdin):
    if check(line, 0):
        ans += 1

print(ans)
