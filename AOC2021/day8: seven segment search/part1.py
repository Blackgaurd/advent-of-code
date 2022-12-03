import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")

# 1: 2 segments
# 4: 4 segments
# 7: 3 segments
# 8: 7 segments
ans = 0
for line in sys.stdin:
    _, nums = line.split('|')
    for num in nums.split():
        if len(num.strip()) in [2, 4, 3, 7]:
            ans += 1

print(ans)
