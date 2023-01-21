t = int(input())
for i in range(t):
    h, w, n = map(int, input().split())
    hh = n % h
    if hh == 0:
        hh = h
    ww = n // h
    if hh == h:
        ww -= 1
    print(hh*100 + ww+1)