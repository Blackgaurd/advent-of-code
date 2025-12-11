import sys
import os
from pathlib import Path
from collections import deque, defaultdict

DIR = Path(os.path.dirname(os.path.abspath(__file__)))
infile = DIR / "input.txt"
sys.stdin = open(infile, "r")


class State:
    def __init__(self, state: int, len: int):
        self.len = len
        self.state = state

    def toggle(self, toggles: list[int]) -> "State":
        new_state = self.state
        for idx in toggles:
            new_state ^= 1 << idx
        return State(new_state, self.len)

    def __str__(self):
        ans = ""
        for idx in range(self.len):
            if (self.state >> idx) & 1:
                ans += "#"
            else:
                ans += "."
        return ans


def parse_state(state: str):
    ret = 0
    len = 0
    for c in reversed(state):
        if c == "#":
            ret <<= 1
            ret |= 1
            len += 1
        elif c == ".":
            ret <<= 1
            len += 1
    return State(ret, len)


def parse_set(toggle: str):
    return list(map(int, toggle[1:-1].split(",")))


def parse_line(line: str):
    state, *toggles, joltage = line.split()
    return parse_state(state), list(map(parse_set, toggles)), parse_set(joltage)


def traverse(target_state: State, toggles: list[list[int]]):
    start_state = State(0, target_state.len)

    dis = defaultdict(lambda: int(1e9))
    dis[start_state.state] = 0
    q = deque([start_state])

    while q:
        cur = q.popleft()
        for toggle in toggles:
            nxt = cur.toggle(toggle)
            if dis[cur.state] + 1 < dis[nxt.state]:
                dis[nxt.state] = dis[cur.state] + 1
                q.append(nxt)

    return dis[target_state.state]


ans = 0
for line in map(lambda ln: ln.strip("\n"), sys.stdin):
    target_state, toggles, _ = parse_line(line)
    cur_ans = traverse(target_state, toggles)
    ans += cur_ans
print(ans)
