import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
visit = [[True] * m for _ in range(n)]
answer = []
q = deque()

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]

for y in range(n):
    for x in range(m):
        if table[y][x] == 1 and visit[y][x] == True:
            q.append([y, x])
            cnt = 0
            while q:
                ny, nx = q.popleft()
                cnt += 1
                visit[ny][nx] = False
                for i in range(4):
                    my = ny + dy[i]
                    mx = nx + dx[i]
                    if 0 <= my < n and 0 <= mx < m and visit[my][mx] == True and table[my][mx] == 1:
                        q.append([my, mx])
                        visit[my][mx] = False
            answer.append(cnt)
if len(answer) == 0:
    print(0)
    print(0)
else:
    print(len(answer))
    print(max(answer))
