import sys
import os
from collections import deque

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")

arr = list(map(int, sys.stdin))
LEN = 25
preamble = deque(arr[:LEN], maxlen=LEN)
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
        print(cur)
        break
    preamble.append(cur)
