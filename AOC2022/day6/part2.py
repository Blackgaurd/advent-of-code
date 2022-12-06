f = open("day6/input.txt", "r")

chars = f.readline().rstrip("\n")
for start in range(len(chars) - 14):
    if len(set(chars[start:start+14])) == 14:
        print(start + 14)
        break

f.close()