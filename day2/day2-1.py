total = 0
with open('input.txt') as f:
    for line in f:
        l, w, h = (int(n) for n in line.split('x'))
        lw, lh, wh = l*w, l*h, w*h
        smallest_size = min(lw, lh, wh)
        surface_area = 2 * (lw + lh + wh)
        total += (smallest_size + surface_area)

print total
