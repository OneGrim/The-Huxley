def difference(array):
    counter = 0
    for l in range(len(array)):
        k, c = 0, 0
        for m in array[l]:
            if m == "C":
                c += 1
            else:
                k += 1
        if abs(k - c) == int(D):
            counter += 1
    return counter
def sample(number):
    return ["C", "K"] if number == 1 else [i + j for i in ["C", "K"] for j in sample(number - 1)]
N, D = input().split()
print(difference(sample(int(N))))
