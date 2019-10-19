mat = []
menor, soma, somandiagonal, countPos = None, 0, 0, 0
for i in range(3):
    row = []
    for j in range(3):
        val = int(input())
        if menor == None or val<menor:
            menor = val
        if(val>0):
            soma += val
            countPos += 1
        somandiagonal += val if i!=j else 0
        row.append(val)
    mat.append(row)
delta = 0 if menor%2 == 1 else 1
print("%.2f"%(soma/countPos)+" "+str(menor)+" "+str(delta)+" "+str(somandiagonal))
