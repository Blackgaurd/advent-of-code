import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part2.txt", "w")


def parse(line: str):
    game, draws = line.split(": ")
    game = int(game.split()[-1])

    p_draws = []
    for d in draws.split("; "):
        cur = {}
        for x in d.split(", "):
            n, c = x.split()
            cur[c] = int(n)
        p_draws.append(cur)

    return game, p_draws


ans = 0
for line in sys.stdin.read().splitlines():
    idx, games = parse(line)
    MX = {"red": 0, "green": 0, "blue": 0}
    for g in games:
        for k, v in g.items():
            MX[k] = max(MX[k], v)

    power = MX["red"] * MX["blue"] * MX["green"]
    ans += power

print(ans)
