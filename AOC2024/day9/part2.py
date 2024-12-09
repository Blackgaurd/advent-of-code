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
id_to_len = dict()
id_to_pos = dict()
free_blocks = []
cur_id = 0
for i, freq in enumerate(encrypt):
    if i % 2 == 0:
        id_to_len[cur_id] = int(freq)
        id_to_pos[cur_id] = len(decrypt)
        for _ in range(int(freq)):
            nonempty_positions.append(len(decrypt))
            decrypt.append(cur_id)
        cur_id += 1
    else:
        free_blocks.append((len(decrypt), int(freq)))
        for _ in range(int(freq)):
            empty_positions.append(len(decrypt))
            decrypt.append(-1)

for move_id in reversed(range(cur_id)):
    want_len = id_to_len[move_id]
    id_pos = id_to_pos[move_id]

    found = False

    # find first large enough block
    for block_i, (block_pos, block_len) in enumerate(free_blocks):
        if block_pos > id_pos:
            break
        if block_len >= want_len:
            for j in range(want_len):
                decrypt[block_pos + j] = move_id
            free_blocks[block_i] = (block_pos + want_len, block_len - want_len)
            found = True
            break

    if found:
        for j in range(want_len):
            decrypt[id_pos + j] = -1

checksum = 0
for i, x in enumerate(decrypt):
    if x == -1:
        continue
    checksum += i * x
print(checksum)
