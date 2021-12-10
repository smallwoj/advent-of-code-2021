import sys
input = [x.strip() for x in sys.stdin.readlines()]
score = 0
bracket_dict = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}
def parse_line(line):
    bracket_stack = []
    for char in line:
        if char in '{[(<':
            bracket_stack.append(char)
        elif char in '}])>':
            if len(bracket_stack) == 0:
                return 0
            if bracket_stack[-1] == '{' and char == '}':
                bracket_stack.pop()
            elif bracket_stack[-1] == '[' and char == ']':
                bracket_stack.pop()
            elif bracket_stack[-1] == '(' and char == ')':
                bracket_stack.pop()
            elif bracket_stack[-1] == '<' and char == '>':
                bracket_stack.pop()
            else:
                return 0
    score = 0
    for char in reversed(bracket_stack):
        score = score * 5 + bracket_dict[char]
    return score
scores = []
for line in input:
    s = parse_line(line)
    if s != 0:
        scores.append(s)

scores.sort()
    
print(scores[len(scores)//2])
