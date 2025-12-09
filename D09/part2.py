def print_floor(floor):
    for y in range(len(floor)):
        for x in range(len(floor[y])):
            print(floor[y][x], end="")
        print()


def draw_line(floor, p1, p2):
    if p1[0] == p2[0]:
        x = p1[0]
        for y in range(min(p1[1], p2[1]) + 1, max(p1[1], p2[1])):
            floor[y][x] = 'X'
    elif p1[1] == p2[1]:
        y = p1[1]
        for x in range(min(p1[0], p2[0]) + 1, max(p1[0], p2[0])):
            floor[y][x] = 'X'


corners = []
with open('input', 'r') as f:
    for line in f:
        corners.append(tuple(map(lambda x: int(x), line.split(','))))

min_x = min(c[0] for c in corners)
max_x = max(c[0] for c in corners)
min_y = min(c[1] for c in corners)
max_y = max(c[1] for c in corners)

new_corners = []
for i in range(len(corners)):
    new_corners.append((corners[i][0] - min_x, corners[i][1] - min_y))

corners = new_corners

floor = []
for y in range(max_y-min_y+1):
    floor.append(['.'] * (max_x-min_x+1))


for i in range(len(corners)):
    x = corners[i][0]
    y = corners[i][1]
    floor[y][x] = '#'
    draw_line(floor, corners[i], corners[(i-1)%len(corners)])
    #print_floor(floor)
    #print()

#print_floor(floor)
