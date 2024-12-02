import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")


def is_increasing(arr):
    for a, b in zip(arr, arr[1:]):
        if a > b:
            return False
    return True


def allow_diffs(arr, min_diff, max_diff):
    for a, b in zip(arr, arr[1:]):
        diff = abs(a - b)
        if min_diff <= diff <= max_diff:
            continue
        return False
    return True


count = 0
for line in sys.stdin.readlines():
    arr = list(map(int, line.split()))
    if (is_increasing(arr) or is_increasing(arr[::-1])) and allow_diffs(arr, 1, 3):
        count += 1

print(count)
