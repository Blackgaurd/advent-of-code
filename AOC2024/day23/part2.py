import sys
import os
from pathlib import Path
from collections import defaultdict

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

adj = defaultdict(set)
for line in map(lambda s: s.strip("\n"), sys.stdin):
    a, b = line.split("-")
    adj[a].add(b)
    adj[b].add(a)


dp = dict()


def largest_full_subgraph(nodes: set[str]) -> set[str]:
    global dp

    if len(nodes) == 1:
        return nodes

    key = tuple(nodes)
    if key in dp:
        return dp[key]

    ret = set()
    for n in nodes:
        marked = adj[n].intersection(nodes)
        largest_with_n = largest_full_subgraph(marked).copy()
        largest_with_n.add(n)

        if len(largest_with_n) > len(ret):
            ret = largest_with_n

    dp[key] = ret
    return ret


largest = list(largest_full_subgraph(set(adj.keys())))
largest.sort()
print(",".join(largest))
