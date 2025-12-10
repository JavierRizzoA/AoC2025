corners = []
with open('input', 'r') as f:
    for line in f:
        corners.append(tuple(map(lambda x: int(x), line.split(','))))


max_area = 0
for i in range(len(corners) - 1):
    for j in range(i + 1, len(corners)):
        area = (abs(corners[i][0] - corners[j][0]) + 1) * (abs(corners[i][1] - corners[j][1]) + 1)
        max_area = max(max_area, area)

print(max_area)
