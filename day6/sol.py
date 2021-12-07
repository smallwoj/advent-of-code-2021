import sys
input = [x.strip() for x in sys.stdin.readlines()]

fishes = [int(x) for x in input[0].split(',')]

# this a naive solution, but it works
days = 80
for day in range(days):
    num_fishes = len(fishes)
    for i in range(num_fishes):
        fishes[i] -= 1
        if fishes[i] < 0:
            fishes[i] = 6
            fishes.append(8)

print(len(fishes))
