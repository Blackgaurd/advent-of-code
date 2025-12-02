import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")

range_strs = input().split(",")
max_num = 0
ranges = []
for start, end in map(lambda rg: rg.split("-"), range_strs):
    ranges.append(range(int(start), int(end) + 1))
    max_num = max(max_num, int(end))

str_max_num = str(max_num)
max_base = max(
    int(str_max_num[: len(str_max_num) // 2]),
    int(str_max_num[-len(str_max_num) // 2 :]),
)

invalid = set()
for base in range(1, max_base + 1):
    base = str(base)
    rep = base
    while True:
        rep += base
        int_rep = int(rep)
        if int_rep > max_num:
            break

        for r in ranges:
            if int_rep in r:
                invalid.add(int_rep)
                break

print(sum(invalid))
