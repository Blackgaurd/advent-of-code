import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")

arr = [l + "." for l in sys.stdin.read().splitlines()]


def check(i, j):
    for ni in [i - 1, i, i + 1]:
        if ni < 0 or ni >= len(arr):
            continue
        for nj in [j - 1, j, j + 1]:
            if nj < 0 or nj >= len(arr[0]):
                continue
            if not (arr[ni][nj].isdigit() or arr[ni][nj] == "."):
                return True
    return False


ans = 0
cur = 0
symbol = False
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j].isdigit():
            cur = cur * 10 + int(arr[i][j])
            symbol = symbol or check(i, j)
        else:
            if symbol:
                ans += cur
            cur = 0
            symbol = False


print(ans)