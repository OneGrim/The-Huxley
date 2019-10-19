# Miguel e Maria Rita
# Pedra= 1, Papel= 2, Tesoura = 3
# Jogador 1 venceu: 1, jogador 2 venceu: 2, empate: 0
def pedraPapelTesoura(j1, j2):
    res = 0
    if j1 == j2:
        res = 0
    elif j1 == "pedra":
        if j2 == "tesoura":
            res = 1
        elif j2 == "papel":
            res = 2
    elif j1 == "papel":
        if j2 == "tesoura":
            res = 2
        elif j2 == "pedra":
            res = 1
    elif j1 == "tesoura":
        if j2 == "pedra":
            res = 2
        elif j2 == "papel":
            res = 1
    return res

count, pontMiguel, pontMaria = 0, 0, 0
for i in range(5):
    MIGUEL, MARIA = str(input()), str(input())
    pontMiguel += 1 if pedraPapelTesoura(MIGUEL, MARIA) == 2 else 0
    pontMaria += 1 if pedraPapelTesoura(MIGUEL, MARIA) == 1 else 0
#print(pontMaria)
#print(pontMiguel)
if(pontMiguel==pontMaria):
    while(pontMiguel==pontMaria):
        MIGUEL, MARIA = str(input()), str(input())
        pontMiguel += 1 if pedraPapelTesoura(MIGUEL, MARIA) == 1 else 0
        pontMaria += 1 if pedraPapelTesoura(MIGUEL, MARIA) == 2 else 0

else:
    print("MIGUEL" if pontMiguel > pontMaria else "MARIA")
