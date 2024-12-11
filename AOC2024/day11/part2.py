import sys
import os
from pathlib import Path
from functools import cache

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

stones = list(map(int, input().split()))
blinks = 75


def blink(stone):
    if stone == 0:
        return [1]
    elif (l := len(str(stone))) % 2 == 0:
        left = stone // 10 ** (l // 2)
        right = stone % 10 ** (l // 2)
        return [left, right]
    return [stone * 2024]


@cache
def dp(start_num, num_blinks):
    if num_blinks == 0:
        return 1

    new_stones = blink(start_num)
    ans = sum(dp(ns, num_blinks - 1) for ns in new_stones)
    return ans


ans = 0
for s in stones:
    ans += dp(s, blinks)
print(ans)
