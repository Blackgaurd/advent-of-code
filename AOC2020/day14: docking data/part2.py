import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part2.txt", "w")


def apply_mask(num, mask):
    ret = ["0" for i in range(len(mask))]
    for i in range(len(mask)):
        if num & (1 << i) != 0:
            ret[i] = "1"
    ret.reverse()
    for i in range(len(mask)):
        if mask[i] == "X":
            ret[i] = "X"
        elif mask[i] == "1":
            ret[i] = "1"
    return ret


nums = []


def get_sum(arr, ind):
    if ind >= len(arr):
        nums.append(int("".join(arr), 2))
        return
    for i in range(ind, len(arr)):
        if arr[i] == "X":
            arr[i] = "1"
            get_sum(arr, i + 1)
            arr[i] = "0"
            get_sum(arr, i + 1)
            arr[i] = "X"
            return
    get_sum(arr, ind + 1)


cur_mask = ""
mem = {}
for line in sys.stdin:
    tokens = line.strip().split()
    if tokens[0] == "mask":
        cur_mask = tokens[2]
    else:
        ind = int(tokens[0][4:-1])
        val = int(tokens[2])
        parsed = apply_mask(ind, cur_mask)
        nums.clear()
        get_sum(parsed, 0)
        for num in nums:
            mem[num] = val

print(sum(mem.values()))
