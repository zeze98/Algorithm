import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
graph = [[] for _ in range(n+1)]

# 정점값 입력 받기
for _ in range(n-1):
    s, e, w = map(int, input().split())
    graph[s].append([e, w])
    graph[e].append([s, w])


def dfs(point, w):
    for i in graph[point]:
        a, b = i
        if dist[a] == -1:
            dist[a] = w + b
            dfs(a, w+b)


dist = [-1] * (n+1)
dist[1] = 0
dfs(1, 0)
start = dist.index(max(dist))

dist = [-1] * (n+1)
dist[start] = 0
dfs(start, 0)
print(max(dist))
