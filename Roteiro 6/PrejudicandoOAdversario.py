val, mat = int(input()), []

for i in range(val):
    mat.append([int(j) for j in str(input()).split()])
res = ""
for k in range(val):
    for m in range(val):
        res += str((mat[m][k] if int(mat[m][k])>0 else mat[m][k]*2))+" "
    res = res[:-1] + "\n"
print(res)
