from collections import deque
import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())

campus = []
visit = [[0]*m for _ in range(n)]

for i in range(n):
    row = list(input().rstrip())
    for j in range(m):
        if row[j] == 'I':
            ob = [i, j]
    campus.append(row)

direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
cnt = 0


def dfs(x, y):
    global cnt
    if 0 <= x < n and 0 <= y < m and not visit[x][y]:
        visit[x][y] = 1
        if campus[x][y] == 'P':
            cnt += 1

        for dx, dy in direc:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny]:
                if campus[nx][ny] != "X":
                    dfs(nx, ny)


dfs(ob[0], ob[1])

if not cnt:
    print("TT")
else:
    print(cnt)
