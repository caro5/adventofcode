with open('input.txt') as f:
    floor = 0
    while True:
        paren = f.read(1)
        if not paren:
            break
        if paren == '(':
            floor += 1
        elif paren == ')':
            floor -= 1
print floor
