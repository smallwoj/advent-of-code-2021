import sys
input = [x.strip() for x in sys.stdin.readlines()]

heightmap = []
for line in input:
    heightmap.append([int(x) for x in line])

s = 0

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
            s += heightmap[i][j] + 1
print(s)
