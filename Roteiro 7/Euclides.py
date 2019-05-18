def calculate(a, d):
    return d if a % d == 0 else calculate(d, a % d)
for i in range(int(input())):
    A, D = input().split()
    print("MDC({},{}) = {}".format(int(A), int(D), calculate(int(A), int(D))))
