ranges = []
fresh_count = 0


def remove_intersect(first, second):
    # Doesn't intersect
    if first is None or second[0] > first[1]:
        return second

    # Completely included
    if second[1] <= first[1]:
        return None

    # Normal intersect
    return (first[1] + 1, second[1])


with open('input', 'r') as f:
    for line in f:
        line = line.strip()

        if line == '':
            break

        ranges.append(tuple(map(lambda x: int(x), line.split('-'))))


ranges.sort(key=lambda x: x[0])

for i in range(len(ranges)):
    if i == 0:
        fresh_count += ranges[i][1] - ranges[i][0] + 1
        continue

    for j in range(i):
        ranges[i] = remove_intersect(ranges[j], ranges[i])
        if ranges[i] is None:
            break

    if ranges[i] is not None:
        fresh_count += ranges[i][1] - ranges[i][0] + 1

print(fresh_count)
