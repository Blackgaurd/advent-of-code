import sys
import os
from pathlib import Path
from collections import deque

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

grid = []
while (line := input()) != "":
    row = []
    for char in line:
        row.extend(list({"#": "##", "O": "[]", ".": "..", "@": "@."}[char]))
    grid.append(row)

moves: list[str] = []
for line in map(lambda l: l.rstrip("\n"), sys.stdin):
    moves.extend(list(line))


def add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


def find_pos(grid):
    for i, row in enumerate(grid):
        for j, x in enumerate(row):
            if x == "@":
                return i, j


def can_move_lr(grid, pos, d):
    while True:
        pos = add(pos, d)
        px, py = pos
        if grid[px][py] == ".":
            return True
        if grid[px][py] == "#":
            return False


def can_move_ud(grid, pos, d):
    check_q = deque([pos])
    checked = set()

    while check_q:
        cur_pos = check_q.popleft()
        nxt = add(cur_pos, d)
        nx, ny = nxt

        if grid[nx][ny] == "#":
            return False
        elif grid[nx][ny] == "[":
            if nxt in checked or add(nxt, (0, 1)) in checked:
                continue
            check_q.append(nxt)
            check_q.append(add(nxt, (0, 1)))
        elif grid[nx][ny] == "]":
            if nxt in checked or add(nxt, (0, -1)) in checked:
                continue
            check_q.append(nxt)
            check_q.append(add(nxt, (0, -1)))

    return True


def can_move(grid, pos, d):
    if d[0] == 0:
        return can_move_lr(grid, pos, d)
    else:
        return can_move_ud(grid, pos, d)


def do_move_lr(grid, pos, d):
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


def do_move_ud(grid, marked_row, d):
    if not marked_row:
        return

    nxt_row = set()
    for cur in marked_row:
        nxt = add(cur, d)
        nx, ny = nxt
        if grid[nx][ny] == "[":
            nxt_row.add(nxt)
            nxt_row.add(add(nxt, (0, 1)))
        elif grid[nx][ny] == "]":
            nxt_row.add(nxt)
            nxt_row.add(add(nxt, (0, -1)))

    do_move_ud(grid, nxt_row, d)

    for cur in marked_row:
        cx, cy = cur
        nxt = add(cur, d)
        nx, ny = nxt

        grid[nx][ny] = grid[cx][cy]
        grid[cx][cy] = "."


def do_move(grid, pos, d):
    if not can_move(grid, pos, d):
        return pos, grid

    if d[0] == 0:
        return do_move_lr(grid, pos, d)
    else:
        do_move_ud(grid, {pos}, d)
        return add(pos, d), grid


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
        if x == "[":
            ans += 100 * i + j

print(ans)
