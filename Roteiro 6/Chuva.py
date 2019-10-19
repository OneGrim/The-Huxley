dim = int(input())
txt , mat1, mat2, matres = "", [], [],[]
for i in range(2):
    for k in range(dim):
        l = [int(j) for j in str(input()).split()]
        if i == 0:
            mat1.append(l)
        else:
            mat2.append(l)


for i in range(dim):
    rres = []
    for j in range(dim):
        rres.append(mat1[i][j]+mat2[i][j])
    matres.append(rres)


for i in range(dim):
    txt = ""
    for j in range(dim):
        txt+=str(matres[i][j])+" "
    print(txt)
