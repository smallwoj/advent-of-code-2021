import sys
input = [x.strip() for x in sys.stdin.readlines()]

numbers = [int(x) for x in input[0].split(',')]
boards = '\n'.join(input[1:]).strip()
boards = boards.split('\n\n')
boards = [x.split('\n') for x in boards]
blots = []
for i in range(len(boards)):
    blots.append([[False for _ in range(5)] for _ in range(5)])
    boards[i] = [[int(y) for y in x.split()] for x in boards[i]]

def sum_unmarked(board_id):
    sum = 0
    for i in range(5):
        for j in range(5):
            if not blots[board_id][i][j]:
                sum += boards[board_id][i][j]
    return sum

def check_bingo(board_id):
    for i in range(5):
        if sum(blots[board_id][i]) == 5:
            return True
        temp = 0
        for j in range(5):
            temp += blots[board_id][j][i]
        if temp == 5:
            return True
    return False

ids = set(range(len(boards)))

for num in numbers:
    for id in range(len(boards)):
        for i in range(5):
            for j in range(5):
                if boards[id][i][j] == num:
                    blots[id][i][j] = True
                    if id in ids and check_bingo(id):
                        ids.remove(id)
                        if len(ids) == 0:
                            print(num*sum_unmarked(id))
                            sys.exit(0)
