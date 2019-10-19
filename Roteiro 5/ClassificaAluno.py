def ClassificaAluno(media, faltas):
    if(faltas <= 10) :
        if (media >=7):
            print("APROVADO ")
        elif (media >= 9.5):
            print("APROVADO COM LOUVOR")
        else:
            print("REPROVADO")
    else:
        print("REPROVADO POR FALTAS")
ClassificaAluno(float(input()), int(input()))
