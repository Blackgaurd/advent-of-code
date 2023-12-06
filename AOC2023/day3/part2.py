import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")

arr = [l + "." for l in sys.stdin.read().splitlines()]


def surrounding_nums(i, j):
    def is_digit(ni, nj):
        if ni < 0 or ni >= len(arr):
            return False
        if nj < 0 or nj >= len(arr[0]):
            return False
        return arr[ni][nj].isdigit()

    ret = []
    if is_digit(i - 1, j):
        ret.append((i - 1, j))
    else:
        if is_digit(i - 1, j - 1):
            ret.append((i - 1, j - 1))
        if is_digit(i - 1, j + 1):
            ret.append((i - 1, j + 1))

    if is_digit(i  + 1, j):
        ret.append((i  + 1, j))
    else:
        if is_digit(i  + 1, j - 1):
            ret.append((i  + 1, j - 1))
        if is_digit(i  + 1, j + 1):
            ret.append((i  + 1, j + 1))

    if is_digit(i, j - 1):
        ret.append((i, j - 1))
    if is_digit(i, j + 1):
        ret.append((i, j + 1))

    return ret

def parse_num(i, j):
    while j - 1 >= 0 and arr[i][j - 1].isdigit():
        j -= 1
    cur = 0
    while arr[i][j].isdigit():
        cur = cur * 10 + int(arr[i][j])
        j += 1
    return cur

ans = 0
for i in range(len(arr)):
    for j in range(len(arr[0])):
        if arr[i][j] == '*':
            nums = surrounding_nums(i, j)
            if len(nums) == 2:
                prod = 1
                for a, b in nums:
                    prod *= parse_num(a, b)
                ans += prod

print(ans)