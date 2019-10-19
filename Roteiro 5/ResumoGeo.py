
quadrados, circulos, retangulos = [], [], []
def calculoFig(tipo):
    res = 
    if (tipo == "q"):
        n = int(input())
        quadrados.append(-1) if (n < 0) else quadrados.append(n * n)
    elif (tipo == "r"):
        l1, l2 = int(input()), int(input())
        retangulos.append(-1) if (l1 < 0 and l2 < 0) else retangulos.append(l1 * l2)
    elif (tipo == "c"):
        raio = int(input())
        circulos.append(-1) if (raio < 0) else circulos.append(3.14 * (raio ** 2))
    else:
        return 0

tipo = "x"
while (tipo != "sair"):
    tipo = str(input())
    calculoFig(tipo)
quadrados.sort()
circulos.sort()
retangulos.sort()
qntFiguras = len(quadrados) + len(circulos) + len(retangulos)
print("Maior circulo: " + "%.2f" % circulos[-1])
print("Maior retangulo: " + "%.2f" % retangulos[-1])
print("Maior quadrado: " + "%.2f" % quadrados[-1])
print("Quantidade de figuras " + str(qntFiguras))
print("Percentual de circulos: " + "%.2f" % ((len(circulos) / qntFiguras) * 100))
