import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"

sys.stdin = open(infile, "r")


def joltage(x: str) -> int:
    ans = 0
    for i in range(len(x)):
        for j in range(i + 1, len(x)):
            cur = x[i] + x[j]
            ans = max(ans, int(cur))
    return ans


ans = 0
for line in map(lambda ln: ln.rstrip("\n"), sys.stdin.readlines()):
    j = joltage(line)
    ans += j
print(ans)
