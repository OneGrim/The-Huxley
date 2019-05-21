def difference(array):
    counter = 0
    for l in range(len(array)):
        if abs(array[l].count("K") - array[l].count("C")) == int(D):
            counter += 1
    return counter
def sample(number):
    return ["C", "K"] if number == 1 else [i + j for i in ["C", "K"] for j in sample(number - 1)]
N, D = input().split()
print(difference(sample(int(N))))
