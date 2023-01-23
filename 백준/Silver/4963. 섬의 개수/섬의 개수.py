import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(x, y):
    dx = [1, 1, 1, -1, -1, -1, 0, 0]
    dy = [1, 0, -1, 1, 0, -1, 1, -1]

    land[x][y] = 0
    for t in range(8):
        nx = x + dx[t]
        ny = y + dy[t]
        if 0 <= nx < h and 0 <= ny < w and land[nx][ny] == 1:
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    land = []
    island = 0
    if w == 0 and h == 0:
        break

    for _ in range(h):
        land.append(list(map(int, input().split())))
    for i in range(h):
        for j in range(w):
            if land[i][j] == 1:
                dfs(i, j)
                island += 1
    print(island)