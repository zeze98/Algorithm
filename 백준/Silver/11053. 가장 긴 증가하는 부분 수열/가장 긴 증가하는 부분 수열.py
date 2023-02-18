import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

d = [0 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1
print(max(d))