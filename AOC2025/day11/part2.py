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
def dfs(cur: str, target: str) -> int:
    global adj

    if cur == target:
        return 1
    if cur not in adj:
        return 0

    ans = 0
    for nxt in adj[cur]:
        ans += dfs(nxt, target)
    return ans


svr_fft = dfs("svr", "fft")
svr_dac = dfs("svr", "dac")
fft_dac = dfs("fft", "dac")
dac_fft = dfs("dac", "fft")
fft_out = dfs("fft", "out")
dac_out = dfs("dac", "out")

print(svr_fft * fft_dac * dac_out + svr_dac * dac_fft * fft_out)
