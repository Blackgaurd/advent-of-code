import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")


def parse(code):
    lo, hi = 0, 127
    for char in code[:7]:
        if char == "B":
            lo = (lo + hi) // 2 + 1
        else:
            hi = (lo + hi) // 2
    x = lo
    lo, hi = 0, 7
    for char in code[7:]:
        if char == "R":
            lo = (lo + hi) // 2 + 1
        else:
            hi = (lo + hi) // 2
    return x, lo


ans = 0
get_id = lambda x: x[0] * 8 + x[1]
for line in sys.stdin:
    ans = max(ans, get_id(parse(line)))

print(ans)
