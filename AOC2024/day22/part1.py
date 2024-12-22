import sys
import os
from pathlib import Path

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


ans = 0
for secret in map(int, sys.stdin):
    for _ in range(STEPS):
        secret = step(secret)
    ans += secret

print(ans)
