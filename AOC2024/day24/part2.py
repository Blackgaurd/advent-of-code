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

# for the first output bit z00, the adder is defined as:
# 1. x00        AND y00 -> next_carry
# 2. x00        XOR y00 -> z00

# for each bit (except z00) in the output, the adder is defined as a unit
# for example, for z01:
# 1. x01        AND y01 -> aaa
# 2. x01        XOR y01 -> bbb
# 3. prev_carry XOR aaa -> z01
# 4. prev_carry AND aaa -> ccc
# 5. aaa        OR  ccc -> next_carry

states = dict()
while line := input():
    s, b = line.split(": ")
    states[s] = b == "1"

num_z_gates = 0
gates = set()
for line in map(lambda s: s.strip("\n"), sys.stdin):
    pattern = r"(.{3}) (XOR|OR|AND) (.{3}) -> (.{3})"
    match = re.match(pattern, line)
    assert match is not None

    s1, op, s2, out = match.groups()
    if s1 > s2:
        s1, s2 = s2, s1

    gates.add((s1, op, s2, out))

    if out.startswith("z"):
        num_z_gates = max(num_z_gates, int(out[1:]))


def find3(s1, op, s2):
    global gates

    if s1 > s2:
        s1, s2 = s2, s1
    for g_s1, g_op, g_s2, g_out in gates:
        if (g_s1, g_op, g_s2) == (s1, op, s2):
            return (g_s1, g_op, g_s2, g_out)

    raise RuntimeError(f"not found: {(s1, op, s2)}")


def find4(s1, op, s2, out):
    global gates

    if s1 > s2:
        s1, s2 = s2, s1
    for g_s1, g_op, g_s2, g_out in gates:
        if (g_s1, g_op, g_s2, g_out) == (s1, op, s2, out):
            return (g_s1, g_op, g_s2, g_out)

    raise RuntimeError(f"not found: {(s1, op, s2, out)}")


def find_out(out):
    global gates

    for g_s1, g_op, g_s2, g_out in gates:
        if g_out == out:
            return (g_s1, g_op, g_s2, g_out)

    raise RuntimeError(f"not found: {out}")


def find_missing_s2(s1, op):
    global gates

    for g_s1, g_op, g_s2, g_out in gates:
        if g_op == op:
            if s1 == g_s1:
                return s2
            elif s1 == g_s2:
                return s1

    raise RuntimeError(f"not found: {(s1, op)}")


def swap_outs(g1, g2):
    return (g1[0], g1[1], g1[2], g2[3]), (g2[0], g2[1], g2[2], g1[3])


def find_z00():
    global gates

    f1 = find3("x00", "AND", "y00")
    f2 = find4("x00", "XOR", "y00", "z00")

    print(f1)
    print(f2)

    gates.remove(f1)
    gates.remove(f2)

    return f1[-1]


marked = []


def find_cell(z, prev_carry):
    x = f"x{z:02}"
    y = f"y{z:02}"
    z = f"z{z:02}"

    f1 = find3(x, "AND", y)
    print(f1)

    f2 = find3(x, "XOR", y)
    print(f2)

    f3 = find4(prev_carry, "XOR", f2[-1], z)
    print(f3)

    f4 = find3(prev_carry, "AND", f2[-1])
    print(f4)

    f5 = find3(f1[-1], "OR", f4[-1])
    print(f5)

    gates.remove(f1)
    gates.remove(f2)
    gates.remove(f3)
    gates.remove(f4)
    gates.remove(f5)

    return f5[-1]


# keep running this and fix where it breaks by hand in input.txt
prev_carry = find_z00()
for z in range(1, num_z_gates):
    prev_carry = find_cell(z, prev_carry)
    print()
