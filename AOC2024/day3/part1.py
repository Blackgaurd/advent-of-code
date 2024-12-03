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
    pattern = r"mul\((\d+),(\d+)\)"
    matches = re.findall(pattern, line)
    return matches


ttl = 0
for line in sys.stdin.readlines():
    pairs = parse(line)
    for a, b in pairs:
        ttl += int(a) * int(b)
print(ttl)
