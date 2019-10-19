linha = int(input())
op = str(input())
for col in range(12):
    l = [int(i) for i in str(input()).split()]
    if (linha == col):
        if(op == "S"):
            print("%.1f"%sum(l))
        else:
            print("%.1f"%(sum(l)/12))
        break
