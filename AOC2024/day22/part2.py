import sys
import os
from pathlib import Path
from itertools import product
from collections import deque

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

STEPS = 2000


def step(secret: int) -> int:
    def mix(value: int):
        nonlocal secret
        secret ^= value

    def prune():
        nonlocal secret
        secret %= 16777216

    mix(secret * 64)
    prune()

    mix(secret // 32)
    prune()

    mix(secret * 2048)
    prune()

    return secret


prices = []
for secret in map(int, sys.stdin):
    cur_prices = [secret % 10]
    for _ in range(STEPS):
        secret = step(secret)
        cur_prices.append(secret % 10)
    prices.append(cur_prices)


def get_deltas(prices: deque[int]):
    it = iter(prices)
    pre = next(it)

    ret = []
    for p in it:
        ret.append(p - pre)
        pre = p

    return tuple(ret)


def gen_deltas_mp(price_arr: list[int]):
    ret = dict()

    cur_prices = deque(maxlen=5)
    for p in price_arr:
        cur_prices.append(p)
        if len(cur_prices) == 5:
            deltas = get_deltas(cur_prices)
            if deltas not in ret:
                ret[deltas] = p

    return ret


delta_maps = [gen_deltas_mp(price_arr) for price_arr in prices]


max_profit = 0
for deltas in product(
    range(-9, 9 + 1), range(-9, 9 + 1), range(-9, 9 + 1), range(-9, 9 + 1)
):
    profit = 0
    for delta_mp in delta_maps:
        profit += delta_mp.get(deltas, 0)
    max_profit = max(max_profit, profit)

print(max_profit)
