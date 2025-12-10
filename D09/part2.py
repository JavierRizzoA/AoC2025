def any_line_intersects(p1, p2, corners):
    sx1 = min(p1[0], p2[0])
    sx2 = max(p1[0], p2[0])
    sy1 = min(p1[1], p2[1])
    sy2 = max(p1[1], p2[1])

    for i in range(len(corners)):
        l1 = corners[i]
        l2 = corners[(i + 1) % len(corners)]
        x1 = min(l1[0], l2[0])
        x2 = max(l1[0], l2[0])
        y1 = min(l1[1], l2[1])
        y2 = max(l1[1], l2[1])
        if x1 == x2:
            if (x1 > sx1 and x1 < sx2) and ((y1 <= sy1 and y2 > sy1) or (y1 < sy2 and y2 >= sy2)):
                return True
        else:
            if (y1 > sy1 and y1 < sy2) and ((x1 <= sx1 and x2 > sx1) or (x1 < sx2 and x2 >= sx2)):
                return True
    return False


corners = []
with open('input', 'r') as f:
    for line in f:
        corners.append(tuple(map(lambda x: int(x), line.split(','))))


max_area = 0
for i in range(len(corners) - 1):
    for j in range(i + 1, len(corners)):
        area = (abs(corners[i][0] - corners[j][0]) + 1) * (abs(corners[i][1] - corners[j][1]) + 1)
        if area > max_area and not any_line_intersects(corners[i], corners[j], corners):
            max_area = max(max_area, area)

print(max_area)
