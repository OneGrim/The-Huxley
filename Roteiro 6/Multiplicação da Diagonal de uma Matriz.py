k = int(input())
while(k!=0):
    mat = [[0 for v in range(4)] for j in range(4)]
    for i in range(4):
        for j in range(4):
            val = int(input())
            mat[j][i] = val
    res = ""


    for p in range(4):
        for v in range(4):
            if (p==v):
                res += str(mat[p][v]*k)+" "
            else:
                res += str(mat[p][v])+" "
        res = res+"\n"
    print(res[:-1])
    k = int(input())
