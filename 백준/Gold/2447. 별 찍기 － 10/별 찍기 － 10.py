n = int(input())

star = [[' ' for _ in range(n)]for _ in range(n)]

def color(size, x, y):
    if size == 1:
        star[y][x] = '*'
    else:
        nsize = size // 3
        for dy in range(3):
            for dx in range(3):
                if dy != 1 or dx != 1:
                    color(nsize, x+dx*nsize, y+dy*nsize)

color(n, 0, 0)
for k in star:
    print(''.join(k))