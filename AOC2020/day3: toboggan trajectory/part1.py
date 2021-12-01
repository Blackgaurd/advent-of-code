import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")

ans = 0
j = 0
for line in sys.stdin:
    if line[j] == '#':
        ans += 1
    j += 3
    j %= len(line) - 1

print(ans)