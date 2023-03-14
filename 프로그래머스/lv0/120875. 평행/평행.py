def gra(a, b):
    return (a[1] - b[1]) / (a[0]-b[0])
def solution(dots):
    dots.sort()
    x1, y1 = dots[0][0], dots[0][1]
    x2, y2 = dots[1][0], dots[1][1]
    x3, y3 = dots[2][0], dots[2][1]
    x4, y4 = dots[3][0], dots[3][1]
    d1 = (x1, y1)
    d2 = (x2, y2)
    d3 = (x3, y3)
    d4 = (x4, y4)
    if gra(d2, d1) == gra(d4, d3):
        return 1
    elif gra(d3, d1) == gra(d4, d2):
        return 1
    elif gra(d4, d1) == gra(d3, d2):
        return 1
    else:
        return 0