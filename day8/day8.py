data = open("data.txt").readlines()
lines = [line.strip() for line in data]

#up, right, down, left
DIR = [(-1,0),(0,1),(1,0),(0,-1)]
R = len(lines)
C = len(lines[0])

p1 = 0
for r in range(R):
    for c in range(C):
        vis = False
        for (dr,dc) in DIR:
            rr = r
            cc = c
            ok = True
            while True:
                rr += dr
                cc += dc
                if not (0<=rr<R and 0<=cc<C):
                    break
                if lines[rr][cc] >= lines[r][c]:
                    ok = False
            if ok:
                vis = True
        if vis:
            p1 += 1
print(p1)