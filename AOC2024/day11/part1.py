import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

stones = input().split()
blinks = 25


def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == "0":
            new_stones.append("1")
        elif (l := len(stone)) % 2 == 0:
            left, right = stone[: l // 2], stone[l // 2 :].lstrip("0")
            if right == "":
                right = "0"
            new_stones.append(left)
            new_stones.append(right)
        else:
            new_stones.append(str(int(stone) * 2024))
    return new_stones


for _ in range(blinks):
    stones = blink(stones)
print(len(stones))
