from collections import deque
import sys

input = sys.stdin.readline

q = []
n, k = map(int, input().split())
table = []
for y in range(n):
    table.append(list(map(int, input().split())))
    for x in range(n):
        if table[y][x] != 0:
            q.append([table[y][x], y, x, 0])
s, x, y = map(int, input().split())

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

q.sort()
q = deque(q)

while q:
    virus, ty, tx, time = q.popleft()
    if time == s:
        break
    for t in range(4):
        ny = ty + dy[t]
        nx = tx + dx[t]
        if 0 <= ny < n and 0 <= nx < n and table[ny][nx] == 0:
            table[ny][nx] = virus
            q.append([virus, ny, nx, time+1])
print(table[x-1][y-1])
