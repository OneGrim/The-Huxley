def cont(num):
    for i in range(num, 0, -1):
        res = ""
        for j in range(i):
            res += str(i) + "-"
        print(res[:-1])


cont(int(input()))
