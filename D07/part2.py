import copy
lines = []

with open('input', 'r') as f:
    for line in f:
        row = []
        for c in line.strip():
            if c == '.':
                row.append(0)
            elif c == 'S':
                row.append(1)
            else:
                row.append(c)
        lines.append(row)


def count_timelines(lines):
    for y in range(len(lines)):
        if y == len(lines) - 1:
            return sum([x for x in lines[y] if isinstance(x, int)])
        for x in range(len(lines[y])):
            if isinstance(lines[y][x], int) and lines[y][x] > 0:
                if lines[y+1][x] == '^':
                    lines[y+1][x-1] += lines[y][x]
                    lines[y+1][x+1] += lines[y][x]
                else:
                    lines[y+1][x] += lines[y][x]


print(count_timelines(lines))
