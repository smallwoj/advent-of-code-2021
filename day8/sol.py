import sys
input = [x.strip() for x in sys.stdin.readlines()]

s = 0
for line in input:
    signal, output = line.split(' | ')
    for i in output.split():
        if len(i) in [2, 3, 4, 7]:
            s += 1

print(s)
