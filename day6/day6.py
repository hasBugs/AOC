line = open("data.txt").readline()

for x in range(len(line)-4):
    if len(set(line[x:x+4])) == 4:
        print(x+4)
        print(set(line[x:x+4]))
        break

for x in range(len(line)-14):
    if len(set(line[x:x+14])) == 14:
        print(x+14)
        print(set(line[x:x+14]))
        break