mat = []
dias = ["Primeiro Sabado","Primeiro Domingo", "Segundo Sabado", "Segundo Domingo", "Terceiro Sabado", "Terceiro Domingo", "Quarto Sabado","Quarto Domingo"]
meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho",
        "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
ideal, dia, mes = None, "",""

for i in range(12):
    mat.append([float(j) for j in str(input()).split()])
    for k in range(8):
        if(ideal == None) or (mat[i][k] < ideal):
            ideal = mat[i][k]
            dia = dias[k]
            mes = meses[i]
if (ideal>0.5):
    print("Proximo ano eu tento denovo...")
else:
    print("O melhor dia e no "+dia+" de "+mes)

