def destroy(matrix, x, y):
    if matrix[x][y] == "_":
        if matrix[x - 1][y] == "&":
            matrix[x - 1][y] = "_"
        if matrix[x + 1 if x + 1 < len(matrix) else 0][y] == "&":
            matrix[x + 1 if x + 1 < len(matrix) else 0][y] = "_"
        if matrix[x][y - 1] == "&":
            matrix[x][y - 1] = "_"
        if matrix[x][y + 1 if y + 1 < len(matrix) else 0] == "&":
            matrix[x][y + 1 if y + 1 < len(matrix) else 0] = "_"
    return matrix
M = []
for i in range(int(input())):
    Row = [i for i in input()]
    M.append(Row)
for j in range(int(input())):
    X, Y = input().split()
    X, Y = int(X), int(Y)
    M = destroy(M, X, Y)
Result = ""
for k in M:
    for l in k:
        Result += l
    Result += "\n"
print(Result[:-1])
