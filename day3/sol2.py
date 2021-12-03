import sys
input = [x.strip() for x in sys.stdin.readlines()]
initial = [x for x in input]

cols = len(input[0])
oxy = None
# oxygen
for i in range(cols):
    ones = 0
    zeros = 0
    mr_filter = None
    for j in range(len(input)):
        if input[j][i] == '1':
            ones += 1
        elif input[j][i] == '0':
            zeros += 1

    if ones < zeros:
        mr_filter = '0'        
    else:
        mr_filter = '1'

    input = list(filter(lambda x: x[i] == mr_filter, input))
    if len(input) == 1:
        oxy = input[0]
        break

# co2
input = initial
co2 = None
for i in range(cols):
    ones = 0
    zeros = 0
    mr_filter = None
    for j in range(len(input)):
        if input[j][i] == '1':
            ones += 1
        elif input[j][i] == '0':
            zeros += 1

    if ones < zeros:
        mr_filter = '1'        
    else:
        mr_filter = '0'

    input = list(filter(lambda x: x[i] == mr_filter, input))
    if len(input) == 1:
        co2 = input[0]
        break

oxy = int(oxy, 2)
co2 = int(co2, 2)
print(oxy*co2)
