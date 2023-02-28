import sys

input = sys.stdin.readline

n, m = map(int, input().split())
bucket = [i for i in range(n+1)]

for _ in range(m):
    i, j = map(int, input().split())
    temp = []
    for t in range(i, j+1):
        temp.append(bucket[t])
    temp = temp[::-1]

    for t in range(i, j+1):
        bucket[t] = temp[t-i]

for t in range(1, n+1):
    print(bucket[t], end=' ')