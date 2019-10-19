def calcPont(cartas):
    pont = 0
    cartas.sort()
    # + Número da menor carta, se estiverem em ordem crescente com distância 1;
    if (cartas[2] - cartas[1] == 1) and (cartas[1] - cartas[0] == 1):
        pont += cartas[0]
    # + 8, se a soma das cartas for 8
    if (sum(cartas) == 8):
        pont += 8
    # + Número da menor carta, se todas forem iguais;
    if (cartas.count(cartas[0]) == 3):
        pont += cartas[0]
    # + Número da menor carta / 2, se existirem apenas duas menores cartas iguais;
    if (cartas.count(cartas[0]) == 2):
        pont += cartas[0] // 2
    # + Número da maior carta / 2, se existirem apenas duas maiores cartas iguais;
    if (cartas.count(cartas[2]) == 2):
        pont += cartas[2] // 2

    return pont


cartasPaes = list(map(int, str(input()).split()))
cartasWilly = list(map(int, str(input()).split()))
pontPaes = calcPont(cartasPaes)
pontWilly = calcPont(cartasWilly)
if (pontPaes == pontWilly):
    print(0)
elif (pontPaes > pontWilly):
    print(1)
else:
    print(2)
