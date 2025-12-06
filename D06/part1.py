import re

lines = []

with open('input', 'r') as f:
    for line in f:
        line = re.sub(r'\s+', ' ', line.strip())
        elements = line.split(' ')
        lines.append(elements)

results = []
operators = lines[-1]
for operator in operators:
    if operator == '+':
        results.append(0)
    else:
        results.append(1)

for line in lines[:-1]:
    for i in range(len(operators)):
        if operators[i] == '+':
            results[i] += int(line[i])
        else:
            results[i] *= int(line[i])

result = sum(results)
print(result)
