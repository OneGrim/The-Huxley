def digit(number):
    if len(number) == 1:
        return number[0]
    else:
        return digit(str(sum(int(number[i]) for i in range(len(number)))))
N, K = input().split()
print(digit(N * int(K)))
