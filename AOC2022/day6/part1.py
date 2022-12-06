f = open("day6/input.txt", "r")

chars = f.readline().rstrip("\n")
for start in range(len(chars) - 4):
    if len(set(chars[start:start+4])) == 4:
        print(start + 4)
        break

f.close()