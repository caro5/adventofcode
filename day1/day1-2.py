with open('input.txt') as f:
    floor, count = 0, 0
    while True:
        paren = f.read(1)
        if not paren:
            break
        count += 1
        if paren == '(':
            floor += 1
        elif paren == ')':
            floor -= 1
        if floor < 0:
            print count
            break
