import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

grid = []
while (line := input()) != "":
    grid.append(list(line))

moves: list[str] = []
for line in map(lambda l: l.rstrip("\n"), sys.stdin):
    moves.extend(list(line))


def find_pos(grid):
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            if x == "@":
                return i, j


def add(t1, t2):
    return (t1[0] + t2[0], t1[1] + t2[1])


def can_move(grid, pos, d):
    while True:
        pos = add(pos, d)
        px, py = pos
        if grid[px][py] == "#":
            return False
        elif grid[px][py] == ".":
            return True


def do_move(grid, pos, d):
    if not can_move(grid, pos, d):
        return pos, grid

    ret_pos = add(pos, d)
    replace_char = "."
    while True:
        px, py = pos
        tmp_char = grid[px][py]
        grid[px][py] = replace_char
        replace_char = tmp_char
        if replace_char == ".":
            break
        pos = add(pos, d)

    return ret_pos, grid


d4 = {
    "^": (-1, 0),
    ">": (0, 1),
    "<": (0, -1),
    "v": (1, 0),
}
pos = find_pos(grid)
for move in moves:
    d = d4[move]
    pos, grid = do_move(grid, pos, d)

ans = 0
for i, row in enumerate(grid):
    for j, x in enumerate(row):
        if x == "O":
            ans += 100 * i + j

print(ans)
