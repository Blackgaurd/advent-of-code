import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

arr1 = []
arr2 = []
for line in sys.stdin.read().splitlines():
    a, b = map(int, line.split())
    arr1.append(a)
    arr2.append(b)

arr1.sort()
arr2.sort()

print(sum(abs(a - b) for a, b in zip(arr1, arr2)))
