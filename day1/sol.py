input = open('input.txt').readlines()

input = [int(x.strip()) for x in input]

num = 0
prev = 0
for i in range(1, len(input)):
    if input[i] > input[i-1]:
        num += 1

print(num)