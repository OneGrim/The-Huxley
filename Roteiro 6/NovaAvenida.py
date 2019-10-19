n, m = [int (i) for i in str(input()).split()]
mat, menorP = [], -1

for j in range(n):
    mat.append([int(y) for y in str(input()).split()])

for row in range(m):
    rua = []
    for col in range(n):
        rua.append(mat[col][row])
    if(menorP == -1)or(sum(rua) < menorP):
        menorP =  sum(rua)
print(menorP)
    
    

