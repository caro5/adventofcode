total = 0
with open('input.txt') as f:
    for line in f:
        sides = [int(n) for n in line.split('x')]
        sides.sort()
        min1, min2 = sides[0], sides[1]
        ribbon_wrap = 2 * (min1 + min2)
        bow = reduce(lambda a, b: a*b, sides)
        total += (ribbon_wrap + bow)

print total
