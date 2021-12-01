import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")

arr = sys.stdin.readlines()

def check(down, right):
    ans = 0
    j = 0
    for i in range(0, len(arr), down):
        if arr[i][j] == '#':
            ans += 1
        j += right
        j %= len(arr[0]) - 1
    return ans

print(check(1, 1) * check(1, 3) * check(1, 5) * check(1, 7) * check(2, 1))
