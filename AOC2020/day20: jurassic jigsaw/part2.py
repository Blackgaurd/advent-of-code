from dataclasses import dataclass
from pathlib import Path
from typing import Literal
import os
from math import isqrt
import re
import sys
from copy import deepcopy
from typing import cast

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

    def get_top_side(self) -> str:
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
        DIM = len(self.grid[0])
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

    def transpose(self):
        DIM = len(self.grid[0])
        new_grid = [["" for i in range(DIM)] for j in range(DIM)]
        for i in range(DIM):
            for j in range(DIM):
                new_grid[i][j] = self.grid[j][i]
        self.grid = ["".join(row) for row in new_grid]

    def transpose_minor(self):
        self.rotate_cw(3)
        self.transpose()
        self.rotate_cw(1)

    def flip_vertical(self):
        self.grid = [s[::-1] for s in self.grid]

    def flip_horizontal(self):
        self.grid.reverse()


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


def orient_corner_bottom_right(corner: Tile, edges: list[Tile]):
    # mutate corner in place
    def check():
        bottom = corner.get_bottom_side()
        bottom_good = False
        for edge in edges:
            edge_sides = edge.get_sides(include_reverse=True)
            if bottom in edge_sides:
                bottom_good = True
                break

        if not bottom_good:
            return False

        right = corner.get_right_side()
        right_good = False
        for edge in edges:
            edge_sides = edge.get_sides(include_reverse=True)
            if right in edge_sides:
                right_good = True
                break

        return right_good

    while not check():
        corner.rotate_cw(1)


def orient_edge_left_bottom_right(edge: Tile, all_tiles: list[Tile]):
    # mutate edge in place
    def check():
        top = edge.get_top_side()
        for other in all_tiles:
            if other._id == edge._id:
                continue

            other_sides = other.get_sides(include_reverse=True)
            if top in other_sides:
                return False

        return True

    while not check():
        edge.rotate_cw(1)


def build_top_left_border(
    corners: list[Tile], edges: list[Tile], all_tiles: list[Tile]
) -> list[list[Tile | None]]:
    # mutates corners and edges list in place
    for c in corners:
        orient_corner_bottom_right(c, edges)
    for e in edges:
        orient_edge_left_bottom_right(e, all_tiles)

    DIM = isqrt(len(all_tiles))
    grid: list[list[Tile | None]] = [[None for i in range(DIM)] for j in range(DIM)]
    grid[0][0] = corners.pop()

    # build right
    for i in range(DIM - 2):
        prev_right = grid[0][i].get_right_side()  # type: ignore
        found_edges = []
        for edge_i, edge in enumerate(edges):
            if edge.get_left_side() == prev_right:
                found_edges.append((edge_i, False))
            elif edge.get_right_side() == prev_right:
                found_edges.append((edge_i, True))

        assert len(found_edges) == 1
        edge_i, flip = found_edges[0]
        grid[0][i + 1] = edges[edge_i]
        if flip:
            grid[0][i + 1].flip_vertical()  # type: ignore
        edges.pop(edge_i)

    for c in corners:
        c.rotate_cw(1)

    found_corners = []
    for corner_i, c in enumerate(corners):
        if c.get_left_side() == grid[0][-2].get_right_side():  # type: ignore
            found_corners.append((corner_i, False))
        elif c.get_bottom_side()[::-1] == grid[0][-2].get_right_side():  # type: ignore
            found_corners.append((corner_i, True))

    assert len(found_corners) == 1
    corner_i, transpose_minor = found_corners[0]
    grid[0][-1] = corners[corner_i]
    if transpose_minor:
        grid[0][-1].transpose_minor()  # type: ignore
    corners.pop(corner_i)

    # build down
    for e in edges:
        e.rotate_cw(3)

    for i in range(DIM - 2):
        prev_bottom = grid[i][0].get_bottom_side()  # type: ignore
        found_edges = []
        for edge_i, edge in enumerate(edges):
            if edge.get_top_side() == prev_bottom:
                found_edges.append((edge_i, False))
            elif edge.get_bottom_side() == prev_bottom:
                found_edges.append((edge_i, True))

        assert len(found_edges) == 1
        edge_i, flip = found_edges[0]
        grid[i + 1][0] = edges[edge_i]
        if flip:
            grid[i + 1][0].flip_horizontal()  # type: ignore
        edges.pop(edge_i)

    for c in corners:
        c.rotate_cw(2)

    found_corners = []
    for corner_i, c in enumerate(corners):
        if c.get_top_side() == grid[-2][0].get_bottom_side():  # type: ignore
            found_corners.append((corner_i, False))
        elif c.get_right_side()[::-1] == grid[-2][0].get_bottom_side():  # type: ignore
            found_corners.append((corner_i, True))

    assert len(found_corners) == 1
    corner_i, transpose_minor = found_corners[0]
    grid[-1][0] = corners[corner_i]
    if transpose_minor:
        grid[-1][0].transpose_minor()  # type: ignore
    corners.pop(corner_i)

    return grid


def build_rest(
    corners: list[Tile],
    edges: list[Tile],
    middles: list[Tile],
    grid: list[list[Tile | None]],
):
    # mutates corners, edges, middles and grid in place
    DIM = len(grid)
    all_tiles = corners + edges + middles
    for i in range(1, DIM):
        for j in range(1, DIM):
            prev_right = grid[i][j - 1].get_right_side()  # type: ignore
            prev_bottom = grid[i - 1][j].get_bottom_side()  # type: ignore

            found_tiles = []
            for other_i, other in enumerate(all_tiles):
                other_copy = deepcopy(other)
                if not found_tiles:
                    for rot in range(4):
                        if (
                            other_copy.get_left_side() == prev_right
                            and other_copy.get_top_side() == prev_bottom
                        ):
                            found_tiles.append((other_i, rot, False))
                        other_copy.rotate_cw(1)

                    other_copy.flip_vertical()
                    for rot in range(4):
                        if (
                            other_copy.get_left_side() == prev_right
                            and other_copy.get_top_side() == prev_bottom
                        ):
                            found_tiles.append((other_i, rot, True))
                        other_copy.rotate_cw(1)

            assert len(found_tiles) == 1

            other_i, rot, flip = found_tiles[0]
            grid[i][j] = all_tiles[other_i]
            if flip:
                grid[i][j].flip_vertical()  # type: ignore
            grid[i][j].rotate_cw(rot)  # type: ignore
            all_tiles.pop(other_i)


def combine_grid(grid: list[list[Tile]]) -> list[str]:
    DIM_GRID = len(grid)
    DIM_TILE = 10

    combined = []
    for grid_row in range(DIM_GRID):
        for tile_row in range(1, DIM_TILE - 1):
            combined.append(
                "".join(
                    grid[grid_row][grid_col].grid[tile_row][1:-1]
                    for grid_col in range(DIM_GRID)
                )
            )

    return combined


def mark_dragon(combined: list[list[str]], x: int, y: int) -> list[list[str]]:
    DRAGON_1 = "                  # "
    DRAGON_2 = "#    ##    ##    ###"
    DRAGON_3 = " #  #  #  #  #  #   "

    ROW_1 = [i for i, x in enumerate(DRAGON_1) if x == "#"]
    ROW_2 = [i for i, x in enumerate(DRAGON_2) if x == "#"]
    ROW_3 = [i for i, x in enumerate(DRAGON_3) if x == "#"]

    if x + 2 >= len(combined):
        return combined
    if y + len(DRAGON_1) >= len(combined[0]):
        return combined

    # mark with *
    if (
        all(combined[x][y + i] in "#$" for i in ROW_1)
        and all(combined[x + 1][y + i] in "#$" for i in ROW_2)
        and all(combined[x + 2][y + i] in "#$" for i in ROW_3)
    ):
        for i in ROW_1:
            combined[x][y + i] = "$"
        for i in ROW_2:
            combined[x + 1][y + i] = "$"
        for i in ROW_3:
            combined[x + 2][y + i] = "$"

    return combined


def mark_all_dragons(combined: list[str]) -> int:
    def rotate_cw(arr: list[list[str]]):
        DIM = len(arr)
        new_arr = []
        for i in range(DIM):
            cur_s = []
            for j in range(DIM):
                cur_s.append(arr[DIM - 1 - j][i])
            new_arr.append(cur_s)
        return new_arr

    def flip_vertical(arr: list[list[str]]):
        return [row[::-1] for row in arr]

    combined_split = [list(row) for row in combined]
    for _ in range(4):
        for x in range(len(combined_split)):
            for y in range(len(combined_split[x])):
                combined_split = mark_dragon(combined_split, x, y)
        combined_split = rotate_cw(combined_split)

    combined_split = flip_vertical(combined_split)
    for _ in range(4):
        for x in range(len(combined_split)):
            for y in range(len(combined_split[x])):
                combined_split = mark_dragon(combined_split, x, y)
        combined_split = rotate_cw(combined_split)

    roughness = 0
    for row in combined_split:
        for x in row:
            if x == "#":
                roughness += 1
    return roughness


tiles = read_tiles()
corners, edges, middle = partition_tiles(tiles)
grid = build_top_left_border(corners, edges, tiles)
build_rest(corners, edges, middle, grid)

grid = cast(list[list[Tile]], grid)
combined = combine_grid(grid)
ans = mark_all_dragons(combined)
print(ans)
