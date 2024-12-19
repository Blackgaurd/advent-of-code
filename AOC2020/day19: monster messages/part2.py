import sys
import os
from pathlib import Path
from dataclasses import dataclass
from collections import defaultdict

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

# language parsing with CYK
# this algorithm can handle loops in productions


@dataclass(frozen=True)
class Symbol:
    val: str
    terminal: bool


Sequence = tuple[Symbol, ...]


def to_symbol(s: str) -> Symbol:
    if s.isdigit():
        return Symbol(s, terminal=False)
    return Symbol(s.strip('"'), terminal=True)


def parse_productions():
    productions: dict[Symbol, list[Sequence]] = defaultdict(list)

    while line := input():
        if line == "8: 42":
            line = "8: 42 | 42 8"
        elif line == "11: 42 31":
            line = "11: 42 31 | 42 11 31"

        p_from, p_outs = line.split(": ")
        p_from = to_symbol(p_from)
        p_outs = p_outs.split(" | ")

        for output in p_outs:
            sequence = tuple(map(to_symbol, output.split()))
            productions[p_from].append(sequence)

    return productions


def parse(word: Sequence, productions: dict[Symbol, list[Sequence]]) -> bool:
    dp = dict()

    def case1(start: int, length: int) -> bool:
        return length == 0

    def case2(a: Symbol, beta: Sequence, start: int, length: int) -> bool:
        if length == 0:
            return False
        if a != word[start]:
            return False
        return recur(beta, start + 1, length - 1)

    def case3(a: Symbol, start: int, length: int) -> bool:
        for gamma in productions[a]:
            if recur(gamma, start, length):
                return True
        return False

    def case4(a: Symbol, beta: Sequence, start: int, length: int) -> bool:
        x1_start = start
        for x1_length in range(length):
            x2_start = start + x1_length
            x2_length = length - x1_length
            if recur((a,), x1_start, x1_length) and recur(beta, x2_start, x2_length):
                return True
        return False

    def recur(seq: Sequence, start: int, length: int) -> bool:
        key = (seq, start, length)
        if key in dp:
            return dp[key]
        dp[key] = False

        if len(seq) == 0:
            dp[key] = case1(start, length)
        elif seq[0].terminal:
            dp[key] = case2(seq[0], seq[1:], start, length)
        elif not seq[0].terminal:
            if len(seq) == 1:
                dp[key] = case3(seq[0], start, length)
            else:
                dp[key] = case4(seq[0], seq[1:], start, length)

        return dp[key]

    start_seq = (Symbol("0", terminal=False),)
    return recur(start_seq, 0, len(word))


def string_to_word(s: str) -> Sequence:
    return tuple(map(to_symbol, s))


productions = parse_productions()
ans = 0
for line in map(lambda s: s.rstrip("\n"), sys.stdin):
    seq = string_to_word(line)
    if parse(seq, productions):
        ans += 1

print(ans)
