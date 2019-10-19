def EstacaoAno(dia, mes):
    if(mes>=9 and dia >=21) or (mes>9 and mes<12) or (mes==12 and dia<=20) :
        return("PRIMAVERA")
    elif(mes == 12 and dia > 20) or (mes>=1 and mes<3) or (mes==3 and dia<=20):
        return("VERAO")
    elif(mes == 3 and dia > 20) or (mes>3 and mes<6) or (mes == 6 and dia<=20):
        return("OUTONO")
    elif(mes == 6 and dia>20) or (mes>6 and mes <9) or (mes == 9 and dia<20):
        return("INVERNO")

print(EstacaoAno(int(input()),int(input())))
