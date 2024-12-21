import sys
import os
from pathlib import Path
import itertools

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

        # chars_needed = x_char * abs(x_delta) + y_char * abs(y_delta)
        # new_paths = [
        #     p
        #     for p in itertools.permutations(chars_needed, len(chars_needed))
        #     if sim(f_pos, p)
        # ]

        # maybe change path creation to permutations of path1

        new_paths = []
        path1 = x_char * abs(x_delta) + y_char * abs(y_delta)
        if sim(f_pos, path1):
            new_paths.append(path1 + "A")

        path2 = y_char * abs(y_delta) + x_char * abs(x_delta)
        if path2 != path1 and sim(f_pos, path2):
            new_paths.append(path2 + "A")

        paths.append(new_paths)

    for p in itertools.product(*paths):
        yield "".join(p)


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


def shortest_seq(seq: str):
    ans = int(1e9)
    for moves1 in gen_numpad_ins(seq, numpad_pos, numpad_empty):
        for moves2 in gen_numpad_ins(moves1, movepad_pos, movepad_empty):
            for moves3 in gen_numpad_ins(moves2, movepad_pos, movepad_empty):
                ans = min(ans, len(moves3))
    return ans


ans = 0
for line in map(lambda s: s.rstrip("\n"), sys.stdin):
    shortest = shortest_seq(line)
    ans += shortest * int(line.rstrip("A"))

print(ans)
