import sys
input = [x.strip() for x in sys.stdin.readlines()]

initial_maze = [[int(x) for x in line] for line in input]
maze = []
for num1 in range(5):
    for y in range(len(initial_maze)):
        maze.append([])
        for num2 in range(5):
            for x in range(len(initial_maze[y])):
                add = initial_maze[y][x]
                mr_number = initial_maze[y][x] + num1 + num2
                while mr_number >= 10:
                    mr_number = mr_number - 9
                maze[-1].append(mr_number)

class Node:
    def __init__(self, risk, x, y):
        self.risk = risk
        self.adjacents = set()
        self.row = x
        self.col = y

    def add_adjacent(self, node):
        self.adjacents.add(node)

    def __str__(self):
        return str((self.risk, self.row, self.col))

    def __repr__(self):
        return self.__str__()

nodes = dict()
for y in range(len(maze)):
    for x in range(len(maze[y])):
        # create the base node
        if (x, y) not in nodes:
            nodes[(x, y)] = Node(maze[y][x], x, y)
        if x > 0:
            if (x-1,y) not in nodes:
                nodes[(x-1, y)] = Node(maze[y][x-1], x-1, y)
            nodes[(x-1, y)].add_adjacent(nodes[(x, y)])
            nodes[(x, y)].add_adjacent(nodes[(x-1, y)])
        if x+1 < len(maze[y]):
            if (x+1,y) not in nodes:
                nodes[(x+1, y)] = Node(maze[y][x+1], x+1, y)
            nodes[(x+1, y)].add_adjacent(nodes[(x, y)])
            nodes[(x, y)].add_adjacent(nodes[(x+1, y)])
        if y > 0:
            if (x,y-1) not in nodes:
                nodes[(x, y-1)] = Node(maze[y-1][x], x, y-1)
            nodes[(x, y-1)].add_adjacent(nodes[(x, y)])
            nodes[(x, y)].add_adjacent(nodes[(x, y-1)])
        if y+1 < len(maze):
            if (x,y+1) not in nodes:
                nodes[(x, y+1)] = Node(maze[y+1][x], x, y+1)
            nodes[(x, y+1)].add_adjacent(nodes[(x, y)])
            nodes[(x, y)].add_adjacent(nodes[(x, y+1)])
        
def print_maze():
    for y in range(len(maze)):
        for x in range(len(maze)):
            print(nodes[(x, y)].risk, end='')
        print()
# print_maze()
paths = {(0,0): [(0,0)]}
def djikstra(start, end):
    visited = set()
    distances = dict()
    for node in nodes.values():
        distances[node] = float('inf')
    distances[start] = 0
    queue = [start]
    while len(queue) > 0:
        node = queue.pop(0)
        if node in visited:
            continue
        visited.add(node)
        for adjacent in node.adjacents:
            if distances[adjacent] > distances[node] + adjacent.risk:
                distances[adjacent] = distances[node] + adjacent.risk
                paths[(adjacent.row, adjacent.col)] = paths[(node.row, node.col)] + [(adjacent.row, adjacent.col)]
            if adjacent not in visited:
                queue.append(adjacent)
                queue = sorted(queue, key=lambda x: distances[x])
    return distances[end]
dr = djikstra(nodes[(0,0)], nodes[(len(initial_maze)-1, len(initial_maze)-1)])
print(dr)
dr = djikstra(nodes[(0,0)], nodes[(len(maze)-1, len(maze[0])-1)])
print(dr)
