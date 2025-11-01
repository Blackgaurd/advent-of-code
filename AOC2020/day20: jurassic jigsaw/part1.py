from dataclasses import dataclass
from pathlib import Path
from typing import Literal
import os
import re
import sys
from functools import reduce

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")


@dataclass
class Tile:
    _id: int
    grid: list[str]

    def get_top_edge(self) -> str:
        return self.grid[0]

    def get_bottom_side(self) -> str:
        return self.grid[-1]

    def get_left_side(self) -> str:
        return "".join(s[0] for s in self.grid)

    def get_right_side(self) -> str:
        return "".join(s[-1] for s in self.grid)

    def get_sides(self, include_reverse: bool) -> list[str]:
        sides = [self.grid[0], self.grid[-1]]
        sides.append("".join(s[0] for s in self.grid))
        sides.append("".join(s[-1] for s in self.grid))

        if include_reverse:
            sides.append(sides[0][::-1])
            sides.append(sides[1][::-1])
            sides.append(sides[2][::-1])
            sides.append(sides[3][::-1])

        return sides

    def _rotate_cw_once(self):
        DIM = 10
        new_grid = []
        for i in range(DIM):
            cur_s = []
            for j in range(DIM):
                cur_s.append(self.grid[DIM - 1 - j][i])
            new_grid.append("".join(cur_s))
        self.grid = new_grid

    def rotate_cw(self, times: Literal[0, 1, 2, 3]):
        for _ in range(times):
            self._rotate_cw_once()

    def flip(self):
        self.grid = [s[::-1] for s in self.grid]


def parse_tile(lines: list[str]) -> Tile:
    tile_id = int(re.findall(r"(\d+)", lines[0])[0])
    return Tile(_id=tile_id, grid=lines[1:])


def read_tiles() -> list[Tile]:
    lines = map(lambda line: line.rstrip("\n"), sys.stdin.readlines())

    tiles = []
    tile_buf = []
    for line in lines:
        if not line:
            tile = parse_tile(tile_buf)
            tiles.append(tile)
            tile_buf.clear()
        else:
            tile_buf.append(line)

    if tile_buf:
        tile = parse_tile(tile_buf)
        tiles.append(tile)

    return tiles


def partition_tiles(tiles) -> tuple[list[Tile], list[Tile], list[Tile]]:
    corners = []
    edges = []
    middles = []
    for t in tiles:
        t_sides = t.get_sides(include_reverse=False)
        connectable = [False] * len(t_sides)
        for other in tiles:
            if other._id == t._id:
                continue

            other_sides = other.get_sides(include_reverse=True)
            for i, t_side in enumerate(t_sides):
                if t_side in other_sides:
                    connectable[i] = True

        num_connectable = sum(connectable)
        if num_connectable == 2:
            corners.append(t)
        elif num_connectable == 3:
            edges.append(t)
        else:
            middles.append(t)

    assert len(corners) == 4
    return corners, edges, middles


tiles = read_tiles()
corners, edges, middle = partition_tiles(tiles)
print(reduce(lambda a, b: a * b, [c._id for c in corners]))
