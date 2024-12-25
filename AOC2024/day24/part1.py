import sys
import os
from pathlib import Path
import re
from collections import defaultdict

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

states = dict()
while line := input():
    s, b = line.split(": ")
    states[s] = b == "1"

reqs = dict()
for line in map(lambda s: s.strip("\n"), sys.stdin):
    pattern = r"(.{3}) (XOR|OR|AND) (.{3}) -> (.{3})"
    match = re.match(pattern, line)
    assert match is not None

    s1, op, s2, dest = match.groups()
    reqs[dest] = (s1, op, s2)


def trace(cur):
    global states, reqs
    if cur in states:
        return states[cur]

    assert cur in reqs
    s1, op, s2 = reqs[cur]
    lhs = trace(s1)
    rhs = trace(s2)

    return dict(
        AND=lambda a, b: a and b, OR=lambda a, b: a or b, XOR=lambda a, b: a != b
    )[op](lhs, rhs)


z_states = []
for k in reqs.keys():
    if k.startswith("z"):
        z_states.append((k, trace(k)))

ans = 0
for _, b in sorted(z_states, reverse=True):
    ans = ans * 2 + int(b)
print(ans)
