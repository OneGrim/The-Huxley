def even(number):
    return [number] if number == 0 else even(number - 1) + [number] if number % 2 == 0 else even(number - 1)
print(*even(int(input())), sep="\n")
