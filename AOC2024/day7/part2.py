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


def check(target, nums, acc=0):
    if not nums:
        return target == acc

    if check(target, nums[1:], acc + nums[0]):
        return True
    if check(target, nums[1:], acc * nums[0]):
        return True
    if check(target, nums[1:], int(str(acc) + str(nums[0]))):
        return True
    return False


ans = 0
for line in sys.stdin.readlines():
    target, *nums, _ = re.split(r":\s|\s", line)
    target = int(target)
    nums = list(map(int, nums))

    if check(target, nums):
        ans += target
print(ans)
