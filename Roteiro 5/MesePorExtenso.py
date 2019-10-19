def calcMes(numMes):
    meses = ["janeiro","fevereiro","marco","abril","maio","junho","julho","agosto","setembo","outubro","novembro","dezembro"]
    return "invalido" if (numMes < 1 or numMes>12) else meses[numMes-1]


print(calcMes(int(input())))
