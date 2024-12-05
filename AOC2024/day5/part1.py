import sys
import os
from pathlib import Path

DIR = Path(os.path.dirname(os.path.abspath(__file__)))

file_basename = Path(sys.argv[0]).stem
infile = DIR / "input.txt"
outfile = DIR / f"{file_basename}.txt"

sys.stdin = open(infile, "r")
sys.stdout = open(outfile, "w")

rules = []
books = []
for line in sys.stdin.readlines():
    if "|" in line:
        rules.append(tuple(map(int, line.split("|"))))
    elif "," in line:
        books.append(list(map(int, line.split(","))))


def check_book(book, rules):
    positions = dict()
    for i, page in enumerate(book):
        positions[page] = i

    for before, after in rules:
        if before not in positions:
            continue
        if after not in positions:
            continue
        if positions[before] > positions[after]:
            return False
    return True


def middle_page(book):
    return book[len(book) // 2]


ans = 0
for book in books:
    if check_book(book, rules):
        ans += middle_page(book)
print(ans)
