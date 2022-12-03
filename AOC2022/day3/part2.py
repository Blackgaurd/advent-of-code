import string

def score(char):
    val = ord(char)
    if ord('a') <= val <= ord('z'):
        return val - ord('a') + 1
    return val - ord('A') + 27

with open("day3/input.txt", "r") as f:
    lines = list(map(lambda l: l.rstrip("\n"), f.readlines()))

    total = 0
    for i in range(0, len(lines), 3):
        a = set(lines[i])
        b = set(lines[i + 1])
        c = set(lines[i + 2])
        for char in string.ascii_letters:
            if all([char in a, char in b, char in c]):
                total += score(char)

    print(total)