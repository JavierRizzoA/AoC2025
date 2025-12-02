def is_valid(pid):
    l = len(pid)
    if l % 2 == 1:
        return True
    if pid[0: int(l / 2)] == pid[int(l / 2) : l]:
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
                invalid_sum += i


print(invalid_sum)
