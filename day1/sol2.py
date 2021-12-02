import sys
input = sys.stdin.readlines()

input = [int(x.strip()) for x in input]

num = 0
prev = 0
for i in range(2, len(input)):
    if input[i] + input[i-1] + input[i-2] > prev and i > 2:
        num += 1
    prev = input[i] + input[i-1] + input[i-2]

print(num)
