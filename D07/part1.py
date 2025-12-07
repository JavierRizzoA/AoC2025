lines = []
split_count = 0

with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        lines.append(list(line.strip()))

for y in range(len(lines)):
    if y == 0:
        continue
    for x in range(len(lines[y])):
        if lines[y-1][x] == '|' or lines[y-1][x] == 'S':
            if lines[y][x] == '.':
                lines[y][x] = '|'
            if lines[y][x] == '^':
                split_count += 1
                if x > 0 and lines[y][x - 1] == '.':
                    lines[y][x - 1] = '|'
                if x < len(lines[y]) - 1 and lines[y][x + 1] == '.':
                    lines[y][x + 1] = '|'

print(split_count)
