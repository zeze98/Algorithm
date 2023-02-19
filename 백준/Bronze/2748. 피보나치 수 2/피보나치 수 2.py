import sys

input = sys.stdin.readline

n = int(input())

p = [0, 1]
if n < 2:
    print(p[n])
else:
    for i in range(2, n+1):
        pn = p[i-2] + p[i-1]
        p.append(pn)
    print(p[-1])