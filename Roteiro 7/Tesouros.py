def move(x, y, matrix):
    ways = list()
    ways.append(x + 1 < len(matrix) and matrix[x + 1][y] != "#")
    ways.append(y + 1 < len(matrix[x]) and matrix[x][y + 1] != "#")
    ways.append(y - 1 >= 0 and matrix[x][y - 1] != "#")
    ways.append(x - 1 >= 0 and matrix[x - 1][y] != "#")
    return any(ways)
def search(x, y, matrix):
    kind = {'b': 1,
            'p': 5,
            'o': 10,
            'd': 50,
            '.': 0,
            '#': 0}
    character = matrix[x][y]
    value = kind[character]
    if not move(x, y, matrix) or matrix[x][y] == "#":
        return value
    else:
        matrix[x][y] = "#"
        first, second, third, fourth = 0, 0, 0, 0
        if y + 1 < len(matrix[x]) and matrix[x][y + 1] != "#":
            first = value + search(x, y + 1, matrix)
        if x + 1 < len(matrix) and matrix[x + 1][y] != "#":
            second = value + search(x + 1, y, matrix)
        if y - 1 >= 0 and matrix[x][y - 1] != "#":
            third = value + search(x, y - 1, matrix)
        if x - 1 >= 0 and matrix[x - 1][y] != "#":
            fourth = value + search(x - 1, y, matrix)
        matrix[x][y] = character
        return max([first, second, third, fourth])
Line, Column = input().split()
if int(Line) <= 10 and int(Column) <= 10:
    Matrix = [[i for i in input()] for l in range(int(Line))]
    print(search(0, 0, Matrix))
