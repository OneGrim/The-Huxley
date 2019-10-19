ops = []
cred, deb = 0, 0
while True:
    op = str(input())
    if (op == "-1"):
        break
    ops.append([int(op.split()[0]), float(op.split()[1])])
for i in (ops):
    cred += i[1] if i[0] == 0 else 0
    deb += i[1] if i[0] == 1 else 0
print("Creditos: R$ " + "%.2f" % deb)
print("Debitos: R$ " + "%.2f" % cred)
print("Saldo: R$ " + "%.2f" % (deb-cred))
