import sys

input = sys.stdin.readline

n, m = map(int, input().split())

bucket = [0 for _ in range(n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    for t in range(i,j+1):
        bucket[t] = k
for i in range(1,n+1):
    print(bucket[i], end=' ')