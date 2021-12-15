import sys
input = [x.strip() for x in sys.stdin.readlines()]

class Node:
    def __init__(self, name):
        self.name = name
        self.adjacents = set()

    def add_adjacent(self, node):
        self.adjacents.add(node)

    def is_big(self):
        return self.name.isupper()

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

nodes = dict()
for line in input:
    node1, node2 = line.split('-')
    if node1 not in nodes:
        nodes[node1] = Node(node1)
    if node2 not in nodes:
        nodes[node2] = Node(node2)
    nodes[node1].add_adjacent(nodes[node2])
    nodes[node2].add_adjacent(nodes[node1])

paths = []
# find all paths from start to end
def find_paths(node: Node, path: list, visited_twice):
    if node.name == 'end':
        path.append(node)
        paths.append(path)
        return
    if node.name == 'start' and node in path:
        return
    
    if node.is_big():
        path.append(node)
    elif node not in path:
        path.append(node)
    elif path.count(node) == 1 and visited_twice is None:
        path.append(node)
        if path.count(node) == 2:
            visited_twice = node
    else:
        return
    

    for adjacent in node.adjacents:
        find_paths(adjacent, path[:], visited_twice)

find_paths(nodes['start'], [], None)
print(len(paths))
