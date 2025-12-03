import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"

sys.stdin = open(infile, "r")


def argmax(s: str, start: int, end: int) -> int:
    best_c = chr(ord("0") - 1)
    best_i = start
    for i in range(start, end):
        if s[i] > best_c:
            best_c = s[i]
            best_i = i
    return best_i


def joltage(line: str) -> int:
    cur_start = 0
    ans = ""
    for rem in range(12):
        cur_end = len(line) - 12 + rem + 1
        i = argmax(line, start=cur_start, end=cur_end)
        cur_start = i + 1
        ans += line[i]
    return int(ans)


ans = 0
for line in map(lambda ln: ln.rstrip("\n"), sys.stdin.readlines()):
    j = joltage(line)
    ans += j
print(ans)
