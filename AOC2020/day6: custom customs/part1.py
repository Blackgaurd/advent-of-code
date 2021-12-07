import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")

arr = sys.stdin.read().split("\n\n")
ttl = 0
for i in arr:
    ans = set(i)
    if '\n' in ans:
        ttl -= 1
    ttl += len(ans)

print(ttl)
