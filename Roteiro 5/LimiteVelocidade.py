def CalculaMulta(kmh):
    if(kmh>50) and (kmh<=55):
        return 230
    elif(kmh >50) and (kmh <= 60):
        return 340
    elif (kmh > 60):
        return (kmh-50)*19.28
    else:
        return 0.0
print("%.2f"%CalculaMulta(int(input())))
