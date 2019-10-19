def ganhouJogo(matrix):
    for i in range(3):
        col = [k[i] for k in matrix]
	#Checando linhas
        if(matrix[i].count(matrix[i][0]) == 3 and matrix[i][0]!="*"):
            return ("Eduardo" if matrix[i][0] == "X" else "Leonardo")+" ganhou o jogo na linha "+(str(i+1))+"."
            #Checando colunas
        elif(col.count(col[0]) == 3 and col[0]!="*"):
            return ("Eduardo" if col[0] == "X" else "Leonardo")+" ganhou o jogo na coluna "+str(i+1)+"."
        #Checando diagonais
    d1 = [matrix[l][l] for l in range(3)]
    d2 = [matrix[v][abs(v-2)] for v in range(3)]
    if(d1.count(d1[0]) == 3 and d1[0] != "*"):
        return ("Leonardo" if d1[0] == "O" else "Eduardo")+" ganhou o jogo na diagonal principal."
    elif(d2.count(d2[0]) ==3 and d2[0] != "*"):
        return ("Leonardo" if d2[0] == "O" else "Eduardo")+" ganhou o jogo na diagonal secundaria."
    else:
        return 0


def casaOcupada(matrix, x, y, simbol):
    return True if matrix[x][y] == "X" or matrix[x][y] == "O" else False




jogo_inicial = [[j for j in str(input()).split()] for i in range(3)]
oo = input()
jogadas = int(input())
for k in range(jogadas):
    jogada = [i for i in str(input()).split()]

    if(int(jogada[2])>2) or (int(jogada[1])>2):
        print("O Dark Souls afetou sua cabeça? Jogue dentro das demarcações do jogo.")

    elif(casaOcupada(jogo_inicial, int(jogada[1]), int(jogada[2]), jogada[0])):
        print(("Eduardo" if jogada[0] == "X" else "Leonardo") + " não trapacei ou então vamos voltar a jogar Dark Souls.")

    else:
        jogo_inicial[int(jogada[1])][int(jogada[2])] = jogada[0]
        print( ("Eduardo" if jogada[0] == "X" else "Leonardo") + " efetuou sua jogada com sucesso.")
    if(ganhouJogo(jogo_inicial) != 0):
        print(ganhouJogo(jogo_inicial))
        break
    elif(k == jogadas-1):
        print("Nem no jogo da velha conseguimos ganhar algo, vamos voltar para o Dark Souls.")

for x in jogo_inicial:
    print(*x, sep=" ")
