def CalculaHospedagem(tipo, dias):
    tipo = str(tipo)
    precoTotal = 0
    if(tipo.upper()=="INDIVIDUAL"):
        precoTotal =  125*dias
    elif(tipo.upper()=="SUÍTE DUPLA"):
        precoTotal =  140*dias
    else:
        precoTotal =  180*dias
    return precoTotal*0.85 if (dias >= 3) else precoTotal
tipo = str(input())
dias = int(input())

print("%.2f"%CalculaHospedagem(tipo,dias))


