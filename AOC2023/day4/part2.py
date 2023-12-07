import sys
import os
import re
from collections import defaultdict

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")

cards = defaultdict(int)
for line in sys.stdin.read().splitlines():
    game, win, scratched = re.split(":|\|", line)
    game_id = int(game.split()[-1])
    win = [int(s) for s in win.split() if s]
    scratched = [int(s) for s in scratched.split() if s]

    cards[game_id] += 1
    matches = 0
    for s in scratched:
        if s in win:
            matches += 1

    for nxt in range(matches):
        cards[game_id + nxt + 1] += cards[game_id]

print(sum(cards.values()))
