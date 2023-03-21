import sys

input = sys.stdin.readline

n, m = map(int, input().split())
bucket = [i for i in range(1, n+1)]

for _ in range(m):
    i, j, k = map(int, input().split())
    bucket[i - 1:j] = bucket[k-1:j] + bucket[i-1:k-1]

print(*bucket)