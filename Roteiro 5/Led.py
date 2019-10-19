def calcular_leds(dig):
    ql = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    sum_leds = 0
    for i in range(len(dig)):
        sum_leds += ql[int(dig[i])]
    return sum_leds


for j in range(int(input())):
    print(str(calcular_leds(str(input()))) + " leds")
