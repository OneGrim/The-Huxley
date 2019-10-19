def sumEhZero(row):
    return 1 if (sum(row) == 0) else 0


mat = []
while True:
    row = str(input())
    if(row == "acabou"):
        break
    else:
        row = [int(i) for i in row.split()]
        mat.append(row)
res =  "Determinante diferente de zero."
for i in range((len(mat))):
    column = [rowc[i] for rowc in mat]
    if (sumEhZero(mat[i])):
        res = "Determinante zero."
        break
    for j in range(len(mat)):
            #Checando as linhas
        if(j!=i):
            if set(mat[j])==set(mat[i]):
                res = "Determinante zero."
                break
            #Checando as colunas
            if set(column)==set([rowc[j] for rowc in mat]):
                res = "Determinante zero."
                break
print(res)
        

    



