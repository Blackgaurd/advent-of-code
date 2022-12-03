import sys
import os
from collections import deque

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")

arr = map(int, input().split(','))

fish = deque([0 for i in range(9)], maxlen=9)
for num in arr:
    # print(num)
    fish[num] += 1

days = 256
for i in range(days):
    birth = fish.popleft()
    fish.append(birth)
    fish[6] += birth

print(sum(fish))
