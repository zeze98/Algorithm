import sys

input = sys.stdin.readline

N, M = map(int, input().split())

listen = set()
for _ in range(N):
    listen.add(input().rstrip())

nosee = set()
for _ in range(M):
    nosee.add(input().rstrip())

ans = sorted(list(listen & nosee))

print(len(ans))
for i in ans:
    print(i)