import sys
import os
from pathlib import Path
from itertools import batched, product

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

line_it = batched(filter(lambda x: x, map(lambda s: s.strip("\n"), sys.stdin)), n=7)
locks = []
keys = []
for sch in line_it:
    heights = [-1] * len(sch[0])
    for i in range(len(sch[0])):
        for row in sch:
            heights[i] += row[i] == "#"

    if sch[0] == ("#" * len(sch[0])):
        locks.append(heights)
    else:
        keys.append(heights)


def all_same(lst):
    return all(x == lst[0] for x in lst)


ans = 0
for lh, kh in product(locks, keys):
    combined = (l + k for l, k in zip(lh, kh))
    if all(x <= 5 for x in combined):
        ans += 1
print(ans)
