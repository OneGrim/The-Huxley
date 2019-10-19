ent = (input()).split()
n, m, o = int(ent[0]), int(ent[1]), int(ent[2])
a, b, c = [],[],[[0 for i in range(n)]for k in range(o)]
for i in range(n):
    a.append([int(j) for j in str(input()).split()])
for j in range(m):
    b.append([int(i) for i in str(input()).split()])

for k in range(n):
    for j in range(o):
        for i in range(m):
            c[k][j] += a[k][i] * b[i][j]

for x in c:
    print(*x, sep=" ")
