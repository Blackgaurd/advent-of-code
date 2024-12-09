import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

encrypt = input()

decrypt = []
empty_positions = []
nonempty_positions = []
cur_id = 0
for i, freq in enumerate(encrypt):
    if i % 2 == 0:
        for _ in range(int(freq)):
            nonempty_positions.append(len(decrypt))
            decrypt.append(cur_id)
        cur_id += 1
    else:
        for _ in range(int(freq)):
            empty_positions.append(len(decrypt))
            decrypt.append(-1)

for empty, nonempty in zip(empty_positions, reversed(nonempty_positions)):
    if empty > nonempty:
        break
    decrypt[empty], decrypt[nonempty] = decrypt[nonempty], decrypt[empty]

checksum = 0
for i, x in enumerate(decrypt):
    if x == -1:
        break
    checksum += i * x
print(checksum)
