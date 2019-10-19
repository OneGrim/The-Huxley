n = int(input())
m = int(input())
mat = []
for i in range(n):
    mat.append([int(j) for j in str(input()).split()])
qcmds = int(input())
cmds = []
for k in range(qcmds):
    cmds.append(str(input()))
x = int(input())
y = int(input())
xf, yf= x,y
for j in range(len(cmds)):
    if(cmds[j] == "C" and mat[xf-1][yf] == 1):
        xf -= 1
    elif(cmds[j] == "B" and mat[xf+1 if xf+1 < n else 0][yf] == 1):
        xf = xf + 1 if xf+1 < n else xf
    elif(cmds[j] =="E" and mat[xf][yf-1] == 1):
        yf -= 1
    elif(cmds[j] == "D" and mat[xf][yf+1 if yf+1 < m else 0] == 1):
        yf = yf+1 if yf+1 < m else yf

print("("+str(xf) +","+str(yf)+")")
