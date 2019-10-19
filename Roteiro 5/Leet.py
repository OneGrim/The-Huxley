def verificarTexto(txt):
    soma = 0
    if txt=="":
        return " "
    else:
        for i in range(len(txt)):
            if(verificarCaracter(txt[i])!= 0) and(verificarCaracter(txt[i])!=None):
                soma+=1
            elif(verificarCaracter(txt[i])==0):
                return -1
    return soma


def verificarCaracter(car):
    leets = ["A","E","I","O","T","S"]
    leetsR = ["@","3","1","0","7","5"]
    if(car.isdigit()):
        return 0
    else:
        for i in range(len(leets)):
            if((car.upper())==leets[i]):
                return leetsR[i]
def inverterTxt(txt):
    res = ""
    for i in range(1,len(txt)+1):
        res+=txt[-i]
    return res

res = ""
num = -1
texto = str(input())
texto = inverterTxt(texto)
num = 0 if (verificarTexto(texto) ==-1) else verificarTexto(texto) if (verificarTexto(texto)!=" ") else " "
if(num !=0) and (num!=" "):
    for i in range(len(texto)):
        if(verificarCaracter(texto[i])!=None):
            res += verificarCaracter(texto[i])
        else:
            res += texto[i]
res = "numeros" if (num == 0) else "vazio"if (num==" ") else res
print(res)
print(num)
