import sys
input = [x.strip() for x in sys.stdin.readlines()]
crabs = [int(x) for x in input[0].split(',')]


print(sum(min([[sum(range(abs(y-x)+1)) for y in crabs] for x in range(max(crabs))], key=lambda x: sum(x))))
