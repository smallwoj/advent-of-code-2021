import sys
input = [x.strip() for x in sys.stdin.readlines()]

frens = []
for line in input:
    frens.append([int(x) for x in line])

def flash(i,j):
    if i < 0 or j < 0 or i >= len(frens) or j >= len(frens[i]):
        return
    frens[i][j] += 1
    if frens[i][j] > 9:
        for k in range(i-1,i+2):
            for l in range(j-1,j+2):
                if (k != i or l != j) and (k >= 0 and l >= 0 and k < len(frens) and l < len(frens[i])) and frens[k][l] <= 9:
                    # if k == 1 and l == 3:
                    #     print(i,j,k,l, frens[k][l])
                    flash(k,l)

n = 100
s = 0
for step in range(n):
    for i in range(len(frens)):
        for j in range(len(frens[i])):
            if frens[i][j] <= 9:
                flash(i,j)
    for i in range(len(frens)):
        for j in range(len(frens[i])):
            if frens[i][j] > 9:
                frens[i][j] = 0
                s += 1

print(s)
