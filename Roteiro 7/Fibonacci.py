def sequence(number):
    return number if number <= 1 else sequence(number - 1) + sequence(number - 2)
print(sequence(int(input()) - 1))
