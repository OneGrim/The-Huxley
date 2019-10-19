def velkmh(v0, ac, t):
    return v0 + ac * t


menor = 0
for i in range(3):
    vel = velkmh(float(input()), float(input()), float(input()))
    if (menor == 0) or (vel < menor):
        menor = vel
print("%.1f" % (menor * 3.6))
