import sys
import os
from pathlib import Path
from collections import deque
from functools import reduce

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"

sys.stdin = open(infile, "r")

lines = [line.strip("\n") for line in sys.stdin]
max_len = max(len(line) for line in lines)
ops = lines.pop()
ops = deque(ops.split())

for line in lines:
    line += " " * (max_len - len(line))


def process(cur_bufs: list[str], op: str) -> int:
    num_len = len(cur_bufs[0])
    nums = []
    for i in range(num_len):
        cur = 0
        for buf in cur_bufs:
            if buf[i] != " ":
                cur = cur * 10 + int(buf[i])
        nums.append(cur)

    if op == "*":
        return reduce(lambda a, b: a * b, nums)
    else:
        return reduce(lambda a, b: a + b, nums)


ans = 0
cur_bufs = ["" for i in range(len(lines))]
for i in range(max_len + 1):
    if i == max_len or all(line[i] == " " for line in lines):
        ans += process(cur_bufs, ops.popleft())
        cur_bufs = ["" for i in range(len(lines))]
    else:
        for j in range(len(cur_bufs)):
            cur_bufs[j] += lines[j][i]
print(ans)
