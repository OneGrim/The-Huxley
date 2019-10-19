k = int(input())
mat = []
res, numRes = "tr(A) =", 0
for i in range(k):
    mat.append([float(j) for j in str(input()).split()])
    res += " ("+"%.2f"%mat[i][i]+") +"
    numRes+= mat[i][i]
print(res[:-1]+"= "+"%.2f"%numRes)
