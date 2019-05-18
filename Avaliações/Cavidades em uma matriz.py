def smallest():
    c = []
    for k in range(X):
        for l in range(Y):
            if M[k][l] < M[k - 1][l - 1] if k - 1 >= 0 and l - 1 >= 0 else M[k][l] + 1:
                if M[k][l] < M[k - 1][l] if k - 1 >= 0 else M[k][l] + 1:
                    if M[k][l] < M[k - 1][l + 1] if k - 1 >= 0 and l + 1 < len(M[0]) else M[k][l] + 1:
                        if M[k][l] < M[k][l - 1] if l - 1 >= 0 else M[k][l] + 1:
                            if M[k][l] < M[k][l + 1] if l + 1 < len(M[0]) else M[k][l] + 1:
                                if M[k][l] < M[k + 1][l - 1] if k + 1 < len(M) and l - 1 >= 0 else M[k][l] + 1:
                                    if M[k][l] < M[k + 1][l] if k + 1 < len(M) else M[k][l] + 1:
                                        if M[k][l] < M[k + 1][l + 1] if k + 1 < len(M) and l + 1 < len(M[0]) else M[k][l] + 1:
                                            c += ["({}, {})".format(k, l)]
    return c
X, Y = int(input()), int(input())
M = [[int(input()) for j in range(Y)] for i in range(X)]
Coordinates = smallest()
print("[", end="")
print(*Coordinates, sep=", ", end="")
print("]")
