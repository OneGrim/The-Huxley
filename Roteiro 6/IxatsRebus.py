def mostrarMatriz(matrix):
    res = ""
    for row in matrix:
        for item in row:
            res += str(item)+" "
        res = res[:-1]+"\n"
    return(res)


def moverFrota(matrix, qr,qc):
    nmatrix = [[0 for i in range(qc)]for j in range(qr)]
    for row in range(qr):
        for col in range(qc):
            if(matrix[row][col] == 1):
                nmatrix[row-1][0 if col+1 == qc else col+1] = 1
    return nmatrix


def jogarBomba(matrix, x, y):
    coords = [[x,y] ,[x-1, y-1] ,[x-1, 0 if (y+1 == len(matrix[0])) else y+1] ,[0 if (x+1 == len(matrix)) else x+1, 0 if(y+1 == len(matrix[0])) else y+1] ,[0 if (x+1 == len(matrix)) else x+1, y-1]]
    for i in range(5):
        matrix[coords[i][0]][coords[i][1]] = 0
    return matrix




n, m = [int (i) for i in str(input()).split()]
k = int(input())
malha_espacial = [[0 for j in range(m)] for i in range(n)]
#coordenadas iniciais da nave
for i in range(k):
    x, y = [int (l) for l in str(input()).split()]
    malha_espacial[x][y] = 1
#printar matrix
print(mostrarMatriz(malha_espacial))
#h = num de ataques
#b = num de bombas por ataque
h, b = [int(j) for j in str(input()).split()]
for j in range(h):
    for l in range(b):
        x, y = [int(h) for h in str(input()).split()]
        malha_espacial = jogarBomba(malha_espacial, x, y)
    malha_espacial = moverFrota(malha_espacial, n, m)
    print(mostrarMatriz(malha_espacial))
    #printar matrix
