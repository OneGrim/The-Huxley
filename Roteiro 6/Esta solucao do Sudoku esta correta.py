def verificarSudoku(mat):
    nums, mats3 = [1, 2, 3, 4, 5, 6, 7, 8, 9], []
    valido = True
    for i in range(9):
        if (nums != sorted(mat[i])):
            valido = False
        ll = []
        for j in range(9):
            ll.append(mat[j][i])
        if (nums != sorted(ll)):
            valido = False

    for i in range(9):
        for k in range(9):
            if (i == 0 or i % 3 == 0) and (k == 0 or k % 3 == 0):
                nlist = []
                for j in range(3):
                    nlist.extend(mat[i + j][k:k + 3])
                if (nums != sorted(nlist)):
                    valido = False

    return "SIM" if valido else "NAO"


k = int(input())
for i in range(k):
    mat = []
    for j in range(9):
        row = [int(n) for n in str(input()).split()]
        mat.append(row)
    print("Instancia "+str(i+1)+"\n"+verificarSudoku(mat) + "\n")
