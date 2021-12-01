import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")

arr = list(map(int, sys.stdin.read().splitlines()))
arr.sort()
nums = {}

for i in range(len(arr)):
    goal = 2020 - arr[i]
    l, r = i + 1, len(arr) - 1
    while l < r:
        if arr[l] + arr[r] == goal:
            print(arr[l] * arr[r] * arr[i])
            break
        elif arr[l] + arr[r] < goal:
            l += 1
        else:
            r -= 1
