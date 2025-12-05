fresh_count = 0

with open('input', 'r') as f:
    is_ids = False
    ranges = []
    for line in f:
        line = line.strip()

        if line == '':
            is_ids = True
            continue

        if not is_ids:
            ranges.append(tuple(map(lambda x: int(x), line.split('-'))))
            continue

        iid = int(line)
        is_fresh = False
        for r in ranges:
            if iid >= r[0] and iid <= r[1]:
                is_fresh = True
                break

        if is_fresh:
            fresh_count += 1

print(fresh_count)
