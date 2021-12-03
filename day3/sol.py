import sys
input = [x.strip() for x in sys.stdin.readlines()]

tot = len(input)
freqs = {i: 0 for i in range(len(input[0]))}

for line in input:
    for i in range(len(line)):
        if int(line[i]):
            freqs[i] += 1

gamma = ''
for i in range(len(input[0])):
    if freqs[i] >= tot / 2:
        gamma += '1'
    else:
        gamma += '0'

epsilon = ''.join(['1' if i == '0' else '0' for i in gamma])

gamma = int(gamma, 2)
epsilon = int(epsilon, 2)
print(gamma*epsilon)

