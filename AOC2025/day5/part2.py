import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"

sys.stdin = open(infile, "r")

ranges = []
for line in map(lambda ln: ln.strip("\n"), sys.stdin.readlines()):
    if not line:
        break

    start, end = map(int, line.split("-"))
    ranges.append([start, end])

ranges.sort()

new_ranges = []
for start, end in ranges:
    new_ranges.append([start, end])
    while len(new_ranges) >= 2:
        cur_start, cur_end = new_ranges[-1]
        prev_start, prev_end = new_ranges[-2]

        if prev_end >= cur_start:
            new_ranges[-2][1] = max(cur_end, prev_end)
            new_ranges.pop()
        else:
            break

ans = 0
for start, end in new_ranges:
    ans += end - start + 1

print(ans)
