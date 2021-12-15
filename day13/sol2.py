import sys
input = '\n'.join([x.strip() for x in sys.stdin.readlines()])

points, instructions = input.split('\n\n')
points = {tuple(map(int, x.split(','))) for x in points.split('\n')}

for line in instructions.split('\n'):
    new_points = set()
    axis, value = line.split(' ')[-1].split('=')
    value = int(value)
    if axis == 'x':
        for point in points:
            if point[0] >= value:
                shift = -2*abs(point[0]-value)
                new_point = (point[0] + shift, point[1])
                new_points.add(new_point)
            else:
                new_points.add(point)
    elif axis == 'y':
        for point in points:
            if point[1] >= value:
                shift = -2*abs(point[1]-value)
                new_point = (point[0], point[1] + shift)
                new_points.add(new_point)
            else:
                new_points.add(point)

    points = new_points

x_max, y_max = max(points, key=lambda x: x[0])

for y in range(y_max + 1):
    for x in range(x_max + 1):
        if (x, y) in points:
            print('█', end='')
        else:
            print(' ', end='')
    print()
