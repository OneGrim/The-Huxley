def VolumeEsfera(raio):
    return (4*3.1416*(raio**3))/3
for i in range(3):
    print("%.2f"%VolumeEsfera(float(input())))
