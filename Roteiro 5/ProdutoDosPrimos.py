def ehPrimo(n):
    divs = 0
    for i in range(1, n):
        if (n % i == 0):
            divs += 1
        if (divs > 1):
            break
    return True if (divs == 1) else False



def calcProd(listaPrimos):
    prod = 1
    for i in range(len(listaPrimos)):
        if not(ehPrimo(listaPrimos[i])):
            return "SEM PRODUTO"
        else: prod*=listaPrimos[i]
    return prod

print(calcProd(list(map(int, str(input()).split()))))
