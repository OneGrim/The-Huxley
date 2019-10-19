def somaSucessiva(num, q):
    soma = 0
    #A função abs(q) calcula o modulo de q
    if(q<0):
        q = abs(q)
        for i in range(q):
            soma -= num
    else:
        for i in range(q):
            soma += num
    return soma
print(somaSucessiva(int(input()), int(input())))
