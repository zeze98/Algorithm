import sys
from collections import deque

input = sys.stdin.readline


def bfs(i):
    visited = [0] * (n+1)
    q.append(i)
    visited[i] = 1
    while q:
        t = q.popleft()
        for v in people[t]:
            if not visited[v]:
                visited[v] = visited[t]+1
                q.append(v)
    return sum(visited)


n, m = map(int, input().split())
people = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    people[a].append(b)
    people[b].append(a)

q = deque()
res = []
for i in range(1, n+1):
    res.append(bfs(i))

print(res.index(min(res))+1)
