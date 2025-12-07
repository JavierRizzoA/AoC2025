import copy
lines = []

with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        lines.append(list(line.strip()))


def count_timelines(lines):
    if len(lines) == 1:
        return 1


    tried_timelines = []
    for x in range(len(lines[0])):
        if lines[0][x] == 'S' or lines[0][x] == '|':
            if lines[1][x] == '^':
                timeline_count = 0
                if x > 0 and lines[1][x-1] == '.' and not x - 1 in tried_timelines:
                    lines_copy = copy.deepcopy(lines[1:])
                    lines_copy[0][x-1] = '|'
                    tried_timelines.append(x - 1)
                    timeline_count += count_timelines(lines_copy)
                if x < len(lines[0]) - 1 and lines[1][x+1] == '.' and not x + 1 in tried_timelines:
                    lines_copy = copy.deepcopy(lines[1:])
                    lines_copy[0][x+1] = '|'
                    tried_timelines.append(x + 1)
                    timeline_count += count_timelines(lines_copy)
                return(timeline_count)
            else:
                lines[1][x] = '|'
                return count_timelines(lines[1:])

timelines = {}

def count_timelines2(lines, x, path):
    if len(lines) == 1:
        timelines[path] = True
        return

    if lines[0][x] == '^':
        if x > 0 and lines[0][x-1] == '.':
            path = path + 'L'
            count_timelines2(lines[1:], x - 1, path)
        if x + 1 < len(lines[0]) and lines[0][x+1] == '.':
            path = path + 'R'
            count_timelines2(lines[1:], x + 1, path)
    else:
        path = path + 'D'
        count_timelines2(lines[1:], x, path)


def count_timelines3(lines):
    paths_and_pos = []
    for y in range(len(lines)):
        if y == 0:
            paths_and_pos.append({'path': 'D', 'pos': lines[y].index('S')})
            continue

        new_paths_and_pos = []
        for pp in paths_and_pos:
            if lines[y][pp['pos']] == '^':
                new_paths_and_pos.append({'path': pp['path'] + 'L', 'pos': pp['pos'] - 1})
                new_paths_and_pos.append({'path': pp['path'] + 'R', 'pos': pp['pos'] + 1})
            else:
                new_paths_and_pos.append({'path': pp['path'] + 'D', 'pos': pp['pos']})

        paths_and_pos = new_paths_and_pos
    return len(paths_and_pos)
    

print(count_timelines3(lines))
