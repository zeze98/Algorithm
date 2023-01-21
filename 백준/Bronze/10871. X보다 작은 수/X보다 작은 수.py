import sys

n ,x = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
ans = []

for i in range(n):
    if A[i] < x:
        ans.append(A[i])

print(*ans)