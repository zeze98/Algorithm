import sys

N, M = map(int, sys.stdin.readline().split())

s = set([sys.stdin.readline()for i in range(N)])
ans = 0
for i in range(M):
    t = sys.stdin.readline()
    if t in s:
        ans += 1

print(ans)