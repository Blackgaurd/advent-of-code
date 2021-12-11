import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(f"{DIR}/input.txt", "r")
sys.stdout = open(f"{DIR}/part1.txt", "w")

cur_mask = ""
mem = {}
for line in sys.stdin:
    tokens = line.strip().split()
    if tokens[0] == "mask":
        cur_mask = tokens[2][::-1]
    else:
        ind = int(tokens[0][4:-1])
        val = int(tokens[2])
        for i in range(len(cur_mask)):
            if cur_mask[i] == "X":
                continue
            elif cur_mask[i] == '1':
                val |= 1 << i
            else:
                val &= ~(1 << i)
        mem[ind] = val

print(sum(mem.values()))
