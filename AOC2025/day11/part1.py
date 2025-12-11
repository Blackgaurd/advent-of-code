import sys
import os
from pathlib import Path
import re
from functools import cache

DIR = Path(os.path.dirname(os.path.abspath(__file__)))
infile = DIR / "input.txt"
sys.stdin = open(infile, "r")

adj = dict()
for line in sys.stdin:
    start, *dests = re.findall(r"[a-z]{3}", line)
    adj[start] = dests


@cache
def dfs(cur: str) -> int:
    global adj

    if cur == "out":
        return 1

    ans = 0
    for nxt in adj[cur]:
        ans += dfs(nxt)
    return ans


print(dfs("you"))
