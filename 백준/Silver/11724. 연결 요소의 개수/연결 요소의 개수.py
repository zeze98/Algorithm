import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)

n, m = map(int, input().split())
line = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v = map(int, input().split())
    line[u].append(v)
    line[v].append(u)

visit = [False] * (1 + n)


def dfs(s, d):
    visit[s] = True

    for j in line[s]:
        if not visit[j]:
            dfs(j, d + 1)


count = 0

for i in range(1, n + 1):
    if not visit[i]:
        if not line[i]:
            count += 1
            visit[i] = True
        else:
            dfs(i, 0)
            count += 1

print(count)