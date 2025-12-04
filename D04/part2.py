def count_adjacent(diagram, x, y):
    adjacent = 0
    for yy in range(y-1, y+2):
        if yy < 0 or yy >= len(diagram):
            continue
        for xx in range(x-1, x+2):
            if xx < 0 or xx >= len(diagram[yy]) or (xx == x and yy == y):
                continue
            if diagram[yy][xx] == '@':
                adjacent += 1
    return adjacent


diagram = []
with open('input', 'r') as f:
    for line in f:
        diagram.append(list(line.strip()))

accessible = 0
any_accessible = True

while any_accessible:
    any_accessible = False
    for y in range(len(diagram)):
        for x in range(len(diagram[y])):
            if diagram[y][x] == '@' and count_adjacent(diagram, x, y) < 4:
                diagram[y][x] = 'x'
                accessible += 1
                any_accessible = True

print(accessible)
