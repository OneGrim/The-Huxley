def calculate(a, d):
    return d if a % d == 0 else calculate(d, a % d)
print(calculate(int(input()), int(input())))
