import sys
import os
from pathlib import Path
import numpy as np
from scipy.optimize import milp, LinearConstraint

DIR = Path(os.path.dirname(os.path.abspath(__file__)))
infile = DIR / "input.txt"
sys.stdin = open(infile, "r")


def parse_set(toggle: str):
    return list(map(int, toggle[1:-1].split(",")))


def parse_line(line: str):
    _, *toggles, joltage = line.split()
    return list(map(parse_set, toggles)), parse_set(joltage)


def solve(toggles: list[list[int]], joltage: list[int]):
    # we can frame it as a linear program
    # for toggles=[[3], [1, 3], [2], [2, 3], [0, 2], [0, 1]],
    #     joltage=[3, 5, 4, 7]
    # we have
    # min 1^T x
    # s.t. A x = joltage^T
    #      x in Z
    # where A = [
    #   [0, 0, 0, 0, 1, 1],
    #   [0, 1, 0, 0, 0, 1],
    #   [0, 0, 0, 1, 1, 0],
    #   [1, 1, 0, 1, 0, 0]
    # ]
    integrality = np.ones(len(toggles))  # all integers
    c = np.ones(len(toggles))
    A = np.zeros((len(joltage), len(toggles)))
    for col in range(len(toggles)):
        for row in toggles[col]:
            A[row][col] = 1
    b = np.array(joltage, dtype=float)
    constraints = LinearConstraint(A, b, b)

    res = milp(c=c, integrality=integrality, constraints=constraints)
    return int(sum(res.x))


ans = 0
for line in map(lambda ln: ln.rstrip("\n"), sys.stdin):
    toggles, joltage = parse_line(line)
    cur_ans = solve(toggles, joltage)
    ans += cur_ans
print(ans)
