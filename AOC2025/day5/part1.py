import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"

sys.stdin = open(infile, "r")

write_ingredients = False
ranges = []
ingredients = []
for line in map(lambda ln: ln.strip("\n"), sys.stdin.readlines()):
    if not line:
        write_ingredients = True
        continue

    if write_ingredients:
        ingredients.append(int(line))
    else:
        start, end = map(int, line.split("-"))
        ranges.append(range(start, end + 1))

ans = 0
for ing in ingredients:
    for r in ranges:
        if ing in r:
            ans += 1
            break
print(ans)
