def qndDigitos(texto):
    countDigitos = 0
    for i in range(len(texto)):
        if(texto[i].isdigit()): countDigitos += 1
    return countDigitos

print(qndDigitos(str(input())))
