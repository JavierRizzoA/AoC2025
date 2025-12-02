def is_valid(pid):
    l = len(pid)
    for size in range(1, int(l / 2) + 1):
        if not l % size == 0:
            continue
        first_segment = pid[0:size]
        valid = False
        for segment_i in range(1, int(l/size)):
            segment = pid[segment_i * size:segment_i * size + size]
            if not first_segment == segment:
                valid = True
                break
        if not valid:
            return False
    return True



invalid_sum = 0


with open('input', 'r') as f:
    content = f.read().strip()
    for id_range in content.split(','):
        start, end = map(lambda x: int(x), id_range.split('-'))
        for i in range(start, end + 1):
            pid = str(i)
            if not is_valid(pid):
                #print(pid)
                invalid_sum += i


print(invalid_sum)
