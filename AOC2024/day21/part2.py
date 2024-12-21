import sys
import os
from pathlib import Path
import itertools
from functools import cache

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")


def gen_numpad_ins(
    seq: str, key_pos: dict[str, tuple[int, int]], empty_cell: tuple[int, int]
):
    def sim(cur, path):
        cy, cx = cur
        for char in path:
            if char == ">":
                cx += 1
            elif char == "<":
                cx -= 1
            elif char == "^":
                cy -= 1
            elif char == "v":
                cy += 1

            if (cy, cx) == empty_cell:
                return False
        return True

    paths = []
    for f, t in zip("A" + seq, seq):
        f_pos = key_pos[f]
        t_pos = key_pos[t]

        y_delta = t_pos[0] - f_pos[0]
        x_delta = t_pos[1] - f_pos[1]

        y_char = "^" if y_delta < 0 else "v"
        x_char = "<" if x_delta < 0 else ">"

        new_paths = []
        path1 = x_char * abs(x_delta) + y_char * abs(y_delta)
        if sim(f_pos, path1):
            new_paths.append(path1 + "A")

        path2 = y_char * abs(y_delta) + x_char * abs(x_delta)
        if path2 != path1 and sim(f_pos, path2):
            new_paths.append(path2 + "A")

        paths.append(new_paths)

    for p in itertools.product(*paths):
        yield p


numpad_pos = {
    "7": (0, 0),
    "8": (0, 1),
    "9": (0, 2),
    "4": (1, 0),
    "5": (1, 1),
    "6": (1, 2),
    "1": (2, 0),
    "2": (2, 1),
    "3": (2, 2),
    "0": (3, 1),
    "A": (3, 2),
}
numpad_empty = (3, 0)

movepad_pos = {"^": (0, 1), "A": (0, 2), "<": (1, 0), "v": (1, 1), ">": (1, 2)}
movepad_empty = (0, 0)


@cache
def shortest_seq(seq: str, steps: int):
    for char in seq:
        assert char in movepad_pos

    # e.g. >>^A
    assert seq[-1] == "A" and seq.count("A") == 1

    if steps == 0:
        return len(seq)

    min_len = int(1e20)
    for moves in gen_numpad_ins(seq, movepad_pos, movepad_empty):
        ttl_len = 0
        for sub_seq in moves:
            ttl_len += shortest_seq(sub_seq, steps - 1)
        min_len = min(min_len, ttl_len)

    return min_len


ans = 0
for line in map(lambda s: s.strip("\n"), sys.stdin):
    min_len = int(1e20)
    for moves in gen_numpad_ins(line, numpad_pos, numpad_empty):
        ttl_len = 0
        for seq in moves:
            ttl_len += shortest_seq(seq, 25)
        min_len = min(min_len, ttl_len)

    ans += min_len * int(line.rstrip("A"))
print(ans)
