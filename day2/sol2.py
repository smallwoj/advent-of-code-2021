import sys
input = sys.stdin.readlines()

coord = (0, 0)
aim = 0

for line in input:
    command, number = line.strip().split(' ')
    number = int(number)
    if command == 'up':
        aim -= number
    elif command == 'down':
        aim += number
    elif command == 'forward':
        coord = (coord[0] + number, coord[1] + aim*number)

print(coord[0] * coord[1])
