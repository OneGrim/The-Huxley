def fact(number):
    return number if number == 1 else number * fact(number - 1)
Sum = 0
for i in range(5):
    Number = int(input())
    if Number > 0 and Number % 3 == 0: Sum += fact(Number)
print(Sum)
