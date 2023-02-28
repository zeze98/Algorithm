import sys

input = sys.stdin.readline

n, m = map(int, input().split())
bucket = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    bucket[i], bucket[j] = bucket[j], bucket[i]

for i in range(1, n+1):
    print(bucket[i], end=' ')