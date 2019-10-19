mat = []
pastel = mat.append([int(i) for i in str(input()).split()])
empada = mat.append([int(i) for i in str(input()).split()])
kibe = mat.append([int(i) for i in str(input()).split()])
precosmat, precosf = [float(i) for i in str(input()).split()], []
for i in range(3):
    sum = 0
    for j in range(4):
        sum += precosmat[j] * mat[i][j]
    precosf.append(sum)
print("\n".join("%.2f"%i for i in precosf))
