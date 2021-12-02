import sys
input = sys.stdin.readlines()

coord = (0, 0)

for line in input:
    command, number = line.strip().split(' ')
    number = int(number)
    if command == 'up':
        coord = (coord[0], max(coord[1] - number, 0))
    elif command == 'down':
        coord = (coord[0], coord[1] + number)
    elif command == 'forward':
        coord = (coord[0] + number, coord[1])

print(coord[0] * coord[1])
