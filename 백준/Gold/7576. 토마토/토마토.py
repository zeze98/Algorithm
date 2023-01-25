import sys
from collections import deque

input = sys.stdin.readline

m, n = map(int, input().split())

box = []
start = deque([])
for _ in range(n):
    box.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            start.append([i, j])


def bfs():
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    while start:
        x, y = start.popleft()

        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                start.append([nx, ny])
                box[nx][ny] = box[x][y] + 1


bfs()
day = 0
for i in box:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    day = max(day, max(i))

print(day - 1)