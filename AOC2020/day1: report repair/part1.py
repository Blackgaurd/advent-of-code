import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")

arr = list(map(int, sys.stdin.read().splitlines()))
arr.sort()

l, r = 0, len(arr) - 1
while l < r:
    if arr[l] + arr[r] == 2020:
        print(arr[l] * arr[r])
        break
    elif arr[l] + arr[r] < 2020:
        l += 1
    else:
        r -= 1
