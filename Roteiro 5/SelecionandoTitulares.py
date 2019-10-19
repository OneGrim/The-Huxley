def calcRend(desempenhoTreino, gols, cansaco, entros):
    vals = [desempenhoTreino, gols, cansaco, entros]
    if(vals.count(0)>=2):
        return 0
    else:
        return (desempenhoTreino*2)+(gols*3.5)+(cansaco*1.5)+(entros*2)
maiores = [0,0,0]
for i in range(5):
    nome = str(input())
    rend = calcRend(int(input()),int(input()),int(input()),int(input()))
    for j in range(3):
        if(rend > maiores[j]):
            maiores.insert(j,rend)
            break
for i in range(3):
    print("%.1f"%maiores[i])
