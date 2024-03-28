from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
world = [list(map(int, input().split())) for _ in range(n)]
visit = [[False]*m for i in range(n)]
q = deque()
answer = 0
dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]
for y in range(n):
    for x in range(m):
        if world[y][x] == 1:
            continue
        if world[y][x] == 0 and visit[y][x] == False:
            q.append([y, x])
            answer += 1
            while q:
                ny, nx = q.popleft()
                visit[ny][nx] = True
                for t in range(4):
                    ty, tx = (ny + dy[t]) % n, (nx + dx[t]) % m
                    if world[ty][tx] == 0 and visit[ty][tx] == False:
                        q.append([ty, tx])
                        visit[ty][tx] = True
print(answer)
