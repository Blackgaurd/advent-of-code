import sys
import os
import re

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")

ans = 0
for line in sys.stdin.read().splitlines():
    game, win, scratched = re.split(":|\|", line)
    win = [int(s) for s in win.split() if s]
    scratched = [int(s) for s in scratched.split() if s]

    occ = 0
    for s in scratched:
        if s in win:
            occ += 1

    if occ != 0:
        ans += 2 ** (occ - 1)

print(ans)
