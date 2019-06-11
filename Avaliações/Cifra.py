def forward(text, move):
    if len(text) == 1:
        if text[0] in Lower:
            for i in range(26):
                if Lower[i] == text[0]:
                    return Lower[(i + move) if i + move < 26 else (i + move) - 26]
        elif text[0] in Upper:
            for i in range(26):
                if Upper[i] == text[0]:
                    return Upper[(i + move) if i + move < 26 else (i + move) - 26]
        else:
            return text[0]
    else:
        if text[0] in Lower:
            for i in range(26):
                if Lower[i] == text[0]:
                    return Lower[(i + move) if i + move < 26 else (i + move) - 26] + forward(text[1:], move)
        elif text[0] in Upper:
            for i in range(26):
                if Upper[i] == text[0]:
                    return Upper[(i + move) if i + move < 26 else (i + move) - 26] + forward(text[1:], move)
        else:
            return text[0] + forward(text[1:], move)
Upper = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
Lower = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
Move, Text = int(input()), input()
while Move > 26:
    Move -= 26
while Move < -26:
    Move += 26
print(forward(Text, Move))
