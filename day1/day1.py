file = open("data.txt")

lines = file.readlines()

deerTotals = []
agg = 0
first = int(lines[0])

for line in lines:
    if line.strip():
        agg += int(line)
    else:
        deerTotals.append(agg)
        if agg > first:
            first = agg
        agg = 0

print(first)
print(sum(sorted(deerTotals)[-3:]))


    