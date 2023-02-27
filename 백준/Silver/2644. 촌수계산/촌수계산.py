import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)

n = int(input())
target_x, target_y = map(int, input().split())

tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)


def dfs(s):
    for i in tree[s]:
        if parent[i] == 0:
            parent[i] = parent[s] + 1
            dfs(i)


dfs(target_x)

if parent[target_y] > 0:
    print(parent[target_y])
else:
    print(-1)