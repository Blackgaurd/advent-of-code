import sys
import os
from collections import deque

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")

arr = list(map(int, sys.stdin))
LEN = 25
preamble = deque(arr[:LEN], maxlen=LEN)
ans = 0
for i in range(LEN, len(arr)):
    cur = arr[i]
    found = False
    for j in range(len(preamble)):
        if found:
            break
        for k in range(j+1, len(preamble)):
            if preamble[j] + preamble[k] == cur:
                found = True
                break
    if not found:
        ans = cur
        break
    preamble.append(cur)

i = 0
ttl = 0
for j in range(len(arr)):
    ttl += arr[j]
    while ttl > ans:
        ttl -= arr[i]
        i += 1
    if ttl == ans:
        subarray = arr[i:j+1]
        print(max(subarray) + min(subarray))
        break
