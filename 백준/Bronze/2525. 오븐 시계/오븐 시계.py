a, b = map(int, input().split())
c = int(input())

t = a*60 + b + c
h = t // 60
m = t % 60
if h >= 24:
    h -= 24
    print(h, m)
else:
    print(h, m)