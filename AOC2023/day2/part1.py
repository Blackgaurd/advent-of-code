import sys
import os

DIR = os.path.dirname(os.path.abspath(__file__))

sys.stdin = open(DIR + "/input.txt", "r")
sys.stdout = open(DIR + "/part1.txt", "w")


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


MX = {"red": 12, "green": 13, "blue": 14}
ans = 0
for line in sys.stdin.read().splitlines():
    idx, games = parse(line)
    flag = True
    for g in games:
        for k, v in g.items():
            if v > MX[k]:
                flag = False

    if flag:
        ans += idx

print(ans)
