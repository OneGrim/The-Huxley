def calcular_digito(dig):
    if (dig == "FIM"):
        return 0
    else:
        mg1, mg2, mg3, val = max([int(i) for i in dig[:3]]), max([int(i) for i in dig[4:7]]), max(
            [int(i) for i in dig[8:11]]), int(dig[-1])
    return 1 if ((mg1 + mg2 + mg3) % 10 == val) else 2


while True:
    res = calcular_digito(str(input()))
    if res == 1:
        print("VALIDO")
    elif res == 2:
        print("INVALIDO")
    else:
        break
