import sys
input = [x.strip() for x in sys.stdin.readlines()]

covered_points = dict()

def create_line_segment(p1, p2):
    if p1[0] == p2[0]:
        for y in range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1):
            if (p1[0], y) not in covered_points:
                covered_points[(p1[0], y)] = 0
            covered_points[(p1[0], y)] += 1
    elif p1[1] == p2[1]:
        for x in range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1):
            if (x, p1[1]) not in covered_points:
                covered_points[(x, p1[1])] = 0
            covered_points[(x, p1[1])] += 1
    else: # nvm its only diagonal
        rise = int((p2[1] - p1[1])/abs(p2[1] - p1[1]))
        run = int((p2[0] - p1[0])/abs(p2[0] - p1[0]))
        while p1 != p2:
            if (p1[0], p1[1]) not in covered_points:
                covered_points[(p1[0], p1[1])] = 0
            covered_points[(p1[0], p1[1])] += 1
            p1 = (p1[0] + run, p1[1] + rise)
        if p2 not in covered_points:
            covered_points[p2] = 0
        covered_points[p2] += 1
        


for line in input:
    p1, p2 = line.split(' -> ')
    p1 = tuple([int(x) for x in p1.split(',')])
    p2 = tuple([int(x) for x in p2.split(',')])
    create_line_segment(p1, p2)

s = 0
for point in covered_points:
    if covered_points[point] >= 2:
        s += 1

print(s)
