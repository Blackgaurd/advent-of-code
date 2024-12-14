import sys
import os
from pathlib import Path
import re
from collections import defaultdict

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


bots = []
for line in sys.stdin:
    px, py, vx, vy = parse_line(line)
    bots.append((px, py, vx, vy))

# grep through part2.txt for "##########"
for tick in range(8000):
    board = [["." for i in range(LEN_X)] for j in range(LEN_Y)]
    for px, py, vx, vy in bots:
        fx = (px + tick * vx) % LEN_X
        fy = (py + tick * vy) % LEN_Y
        board[fy][fx] = "#"

    #! uncomment the following to run
    # print("TICK:", tick)
    # for row in board:
    #     print("".join(row))
    # print()
