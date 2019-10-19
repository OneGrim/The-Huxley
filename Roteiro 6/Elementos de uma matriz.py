v = str(input()).split()
linhas, col, mat, matP = int(v[0]), int(v[1]), [], ""
diagPri, diagSec, men0, mai0 = 0, 0, 0, 0
for i in range(linhas):
    row = []
    for j in range(col):
        val = int(input())
        diagPri += val if i == j else 0
        diagSec += val if i + j == linhas-1 else 0
        men0 += 1 if val<0 else 0
        mai0 += 1 if val>0 else 0
        row.append(val)
        matP += str(val) + " "
    matP = matP[:-1] + "\n"
    mat.append(row)

print("Matriz formada:\n" + matP[:-1])
if (col == linhas):
    print("A diagonal principal e secundaria tem valor(es) " + str(diagPri) + " e " + str(diagSec) + " respectivamente.")
else:
    print("A diagonal principal e secundaria nao pode ser obtida.")
print("A matriz possui "+str(men0)+" numero(s) menor(es) que zero.")
print("A matriz possui "+str(mai0)+" numero(s) maior(es) que zero.")
