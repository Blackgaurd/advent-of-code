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

LEN_X = 101
LEN_Y = 103


def parse_line(line):
    pattern = r"-?\d+"
    return map(int, re.findall(pattern, line))


quads = [0, 0, 0, 0]
time = 100
for line in sys.stdin:
    px, py, vx, vy = parse_line(line)

    fx = (px + 100 * vx) % LEN_X
    fy = (py + 100 * vy) % LEN_Y

    left = fx < LEN_X // 2
    right = fx > LEN_X // 2
    top = fy < LEN_Y // 2
    bottom = fy > LEN_Y // 2

    if left and top:
        quads[0] += 1
    elif left and bottom:
        quads[1] += 1
    elif right and top:
        quads[2] += 1
    elif right and bottom:
        quads[3] += 1

print(quads[0] * quads[1] * quads[2] * quads[3])
