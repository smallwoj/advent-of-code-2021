import sys
input = [x.strip() for x in sys.stdin.readlines()]
score = 0
bracket_dict = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
def parse_line(line):
    bracket_stack = []
    for char in line:
        if char in '{[(<':
            bracket_stack.append(char)
        elif char in '}])>':
            if len(bracket_stack) == 0:
                return bracket_dict[char]
            if bracket_stack[-1] == '{' and char == '}':
                bracket_stack.pop()
            elif bracket_stack[-1] == '[' and char == ']':
                bracket_stack.pop()
            elif bracket_stack[-1] == '(' and char == ')':
                bracket_stack.pop()
            elif bracket_stack[-1] == '<' and char == '>':
                bracket_stack.pop()
            else:
                return bracket_dict[char]
    return 0
for line in input:
    score += parse_line(line)
    
print(score)
