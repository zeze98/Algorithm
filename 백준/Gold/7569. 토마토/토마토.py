import sys
from collections import deque

input = sys.stdin.readline

m, n, h = map(int, input().split())

box = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]
start = deque([])

for i in range(h):
    for j in range(n):
        for k in range(m):
            if box[i][j][k] == 1:
                start.append([i, j, k])


def bfs():
    dx = [1, -1, 0, 0, 0, 0]
    dy = [0, 0, 1, -1, 0, 0]
    dz = [0, 0, 0, 0, 1, -1]
    while start:
        z, y, x = start.popleft()

        for t in range(6):
            nx = x + dx[t]
            ny = y + dy[t]
            nz = z + dz[t]
            if 0 <= nx < m and 0 <= ny < n and 0 <= nz < h and box[nz][ny][nx] == 0:
                start.append([nz, ny, nx])
                box[nz][ny][nx] = box[z][y][x] + 1


bfs()
day = 0
for i in box:
    for j in i:
        for k in j:
            if k == 0:
                print(-1)
                exit(0)
        day = max(day, max(j))

print(day - 1)
