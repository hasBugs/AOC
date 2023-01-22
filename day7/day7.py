from collections import defaultdict

lines = open('data.txt').readlines()

SZ = defaultdict(int)
path = []
for line in lines:
    words = line.split()
    if words[1] == 'cd':
        if words[2] == '..':
            path.pop()
        else:
            path.append(words[2])
        print(path)
    elif words[1] == 'ls':
        continue
    elif words[0] == 'dir':
        continue
    else:
        sz = int(words[0])

        for i in range(1, len(path)+1):
            SZ['/'.join(path[:i])] += sz
        

# for k, v in SZ.items():
#     print(v)

