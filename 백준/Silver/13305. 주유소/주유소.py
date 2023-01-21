import sys

n = int(input())
d = list(map(int, sys.stdin.readline().split()))
p = list(map(int, sys.stdin.readline().split()))
a = 0
lp = p[0]

for i in range(n-1):
    if p[i] < lp:
        lp = p[i]
    a += lp * d[i]
print(a)