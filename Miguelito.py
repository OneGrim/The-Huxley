def sequence(number):
    return 3 if number == 1 else sequence(number - 1) + 4 if number % 2 == 0 else sequence(number - 1) + 1
print(sequence(int(input())))
