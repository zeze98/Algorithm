import sys

input = sys.stdin.readline
sys.setrecursionlimit(10 ** 9)
n = int(input())

tree = [[] for _ in range(n + 1)]
parent = [0 for _ in range(n + 1)]

for _ in range(n - 1):
    x, y = map(int, input().split())
    tree[x].append(y)
    tree[y].append(x)


def dfs(s, tree, parent):
    for i in tree[s]:
        if parent[i] == 0:
            parent[i] = s
            dfs(i, tree, parent)


dfs(1, tree, parent)

for i in range(2, n + 1):
    print(parent[i])