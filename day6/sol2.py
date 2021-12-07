import sys
input = [x.strip() for x in sys.stdin.readlines()]

fishes = [int(x) for x in input[0].split(',')]

fish_dict = {i: 0 for i in range(9)}
for fish in fishes:
    fish_dict[fish] += 1

days = 256
for day in range(days):
    new_fish_dict = {i: 0 for i in range(9)}
    for i in range(9):
        if i == 0:
            new_fish_dict[6] += fish_dict[i]
            new_fish_dict[8] += fish_dict[i]
        else:
            new_fish_dict[i-1] += fish_dict[i]
    fish_dict = new_fish_dict

print(sum(fish_dict.values()))
