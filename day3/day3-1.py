def check_dir(dir, x, y):
    if dir == '^':
        return x, y + 1
    if dir == '<':
        return x - 1, y
    if dir == '>':
        return x + 1, y
    if dir == 'v':
        return x, y - 1

with open('input.txt') as f:
    visited_houses = 1
    x, y = 0, 0
    grid = {}
    grid[0] = [0]
    while True:
        dir = f.read(1)
        if not dir:
            print visited_houses
            break
        if dir == '\n':
            continue
        x, y = check_dir(dir, x, y)
        if x in grid:
            if y not in grid[x]:
                visited_houses += 1
                grid[x].append(y)
        else:
            grid[x] = [y]
            visited_houses += 1
