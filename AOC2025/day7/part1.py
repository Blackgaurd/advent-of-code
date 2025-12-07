import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"

sys.stdin = open(infile, "r")

beams = set()
splits = 0
for i, c in enumerate(sys.stdin.readline()):
    if c == "S":
        beams.add(i)
        break

for line in sys.stdin.readlines():
    new_beams = beams.copy()
    for beam in beams:
        if line[beam] == "^":
            splits += 1
            new_beams.remove(beam)
            new_beams.add(beam - 1)
            new_beams.add(beam + 1)
    beams = new_beams

print(splits)
