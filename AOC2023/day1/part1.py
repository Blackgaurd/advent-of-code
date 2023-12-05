import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")

ans = 0
for line in sys.stdin.read().splitlines():
    nums = []
    for char in line:
        if char.isdigit():
            nums.append(int(char))
    if nums:
        ans += 10 * nums[0] + nums[-1]

print(ans)
