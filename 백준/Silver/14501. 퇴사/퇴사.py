import sys

input = sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
d = [0 for _ in range(n+1)]

for i in range(n):
    for j in range(i + table[i][0],n+1):
        if d[j] < d[i] + table[i][1]:
            d[j] = d[i] + table[i][1]

print(d[-1])
