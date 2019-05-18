def binary(number):
    return str(number) if int(number) < 2 else str(int(number) % 2) + binary(int(number) // 2)
print(*binary(input())[::-1], sep="\n")
