def gather(first, second, f, s, one = 0, two = 0):
    return first + second if (one if s <= f else two) == (s if s <= f else f) else first[0] + second[0] + gather(first[1:], second[1:], f, s, one + 1, two + 1)
for i in range(int(input())):
    First, Second = input().split()
    print(gather(First.upper(), Second.lower(), len(First), len(Second)))
