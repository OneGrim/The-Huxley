def function(number):
    if len(number) == 1:
        return int(number[0]) * (2 if int(number[0]) % 2 == 0 else 3) * 1
    else:
        return (int(number[0]) * (2 if int(number[0]) % 2 == 0 else 3) * len(number)) + function(number[1:])
while True:
    N = input()
    if int(N) == 0: break
    print(function(N))
