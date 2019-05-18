def even(number):
    if len(number) == 1:
        return 1 if int(number) % 2 == 0 else 0
    else:
        return even(number[1:]) + 1 if int(number[0]) % 2 == 0 else even(number[1:])
print(even(input()))
