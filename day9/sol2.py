import sys
input = [x.strip() for x in sys.stdin.readlines()]

heightmap = []
for line in input:
    heightmap.append([int(x) for x in line])

lowest = []

for i in range(len(heightmap)):
    for j in range(len(heightmap[i])):
        valid = True
        for k in range(-1, 2):
            for l in range(-1, 2):
                if k == 0 and l == 0:
                    continue
                try:
                    if i+k < 0 or i+k >= len(heightmap) or j+l < 0 or j+l >= len(heightmap[i]):
                        continue
                    if heightmap[i+k][j+l] < heightmap[i][j]:
                        valid = False
                except IndexError:
                    pass
        if valid:
            lowest.append((i, j))
sizes = []
for p in lowest:
    size = 0
    to_check = set()
    seen = set()
    to_check.add(p)
    while to_check:
        curr = to_check.pop()
        size += 1
        seen.add(curr)
        if curr[0] + 1 < len(heightmap) and (curr[0] + 1, curr[1]) not in seen and heightmap[curr[0] + 1][curr[1]] > heightmap[curr[0]][curr[1]]:
            if heightmap[curr[0] + 1][curr[1]] != 9:
                to_check.add((curr[0] + 1, curr[1]))
        if curr[0] - 1 >= 0 and (curr[0] - 1, curr[1]) not in seen and heightmap[curr[0] - 1][curr[1]] > heightmap[curr[0]][curr[1]]:
            if heightmap[curr[0] - 1][curr[1]] != 9:
                to_check.add((curr[0] - 1, curr[1]))
        if curr[1] + 1 < len(heightmap[curr[0]]) and (curr[0], curr[1] + 1) not in seen and heightmap[curr[0]][curr[1] + 1] > heightmap[curr[0]][curr[1]]:
            if heightmap[curr[0]][curr[1] + 1] != 9:
                to_check.add((curr[0], curr[1] + 1))
        if curr[1] - 1 >= 0 and (curr[0], curr[1] - 1) not in seen and heightmap[curr[0]][curr[1] - 1] > heightmap[curr[0]][curr[1]]:
            if heightmap[curr[0]][curr[1] - 1] != 9:
                to_check.add((curr[0], curr[1] - 1))

    sizes.append(size)
sizes.sort(reverse=True)
print(sizes[0] * sizes[1] * sizes[2])
