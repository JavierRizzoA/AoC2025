import re

lines = []
empty_cols = {}

def is_empty_col(lines, col):
    if col in empty_cols:
        return empty_cols[col]

    for line in lines:
        if not line[col] == ' ':
            empty_cols[col] = False
            return False

    empty_cols[col] = True
    return True


with open('input', 'r') as f:
    for line in f:
        lines.append(line.strip('\n'))


problems = []

for line in lines[:-1]:
    operand_index = 0
    problem_index = 0
    for c in range(len(line)):
        if is_empty_col(lines, c):
            problem_index += 1
            operand_index = 0
            continue
        if len(problems) <= problem_index:
            problems.append([])
        if len(problems[problem_index]) <= operand_index:
            problems[problem_index].append('')
        if line[c] == ' ':
            operand_index += 1
            continue
        problems[problem_index][operand_index] += line[c]
        operand_index += 1


result = 0
operators = re.sub(r'\s+', ' ', lines[-1]).split(' ')
for p in range(len(problems)):
    p_result = 0
    operator = operators[p]
    if operator == '*':
        p_result = 1
    for n in problems[p]:
        if operator == '+':
            p_result += int(n)
        else:
            p_result *= int(n)
    result += p_result

print(result)
