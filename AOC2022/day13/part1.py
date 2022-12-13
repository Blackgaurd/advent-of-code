f = open("day13/input.txt", "r")

lines = f.readlines()
parse_iter = zip(*[map(lambda x: x.rstrip("\n").strip(), lines)] * 3)


def compare(a, b):
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return 1
        elif a > b:
            return -1
        return 0
    elif isinstance(a, int):
        a = [a]
    elif isinstance(b, int):
        b = [b]

    for i in range(min(len(a), len(b))):
        comp = compare(a[i], b[i])
        if comp != 0:
            return comp

    if len(a) < len(b):
        return 1
    elif len(a) > len(b):
        return -1
    return 0


ans = 0
for i, group in enumerate(parse_iter, start=1):
    a = eval(group[0])
    b = eval(group[1])

    comp = compare(a, b)
    if comp == 1:
        ans += i
    elif comp == 0:
        print("bruh")

print(ans)

f.close()
