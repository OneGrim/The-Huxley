def AnalisarSituacao(notas):
    media = (notas[0] * 1 + notas[1] * 2 + notas[2] * 3 + notas[3] * 4) / 10
    return "reprovado" if (media < 3) else "prova final" if (media < 7) else "aprovado" if (
        media < 9) else "aprovado com louvor"


notas = [float(i) for i in str(input()).split()]
print(AnalisarSituacao(notas))
