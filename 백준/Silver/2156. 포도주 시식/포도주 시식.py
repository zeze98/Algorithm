import sys

input = sys.stdin.readline

n = int(input())
wine = [0]
for _ in range(n):
    wine.append(int(input()))
d = [0, wine[1]]

if n > 1:
    d.append(wine[1] + wine[2])
for i in range(3, n + 1):
     d.append(max(d[i-1], d[i-3] + wine[i-1] + wine[i], d[i-2] + wine[i]))

print(d[n])
