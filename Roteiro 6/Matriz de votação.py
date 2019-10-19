prin = int(input())
eleit, matriz = int(input()), []
for i in range(eleit):
    matriz.append(str(input()).split())
for j in range(prin):
    contVotos = 0
    for k in range(eleit):
        contVotos += 1 if (matriz[k][j]) == "1" else 0
    print("Princesa "+str(j+1)+": "+str(contVotos)+" voto(s)")
