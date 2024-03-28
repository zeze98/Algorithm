from collections import deque
import sys

input = sys.stdin.readline

test_case = int(input())
dx = [2, 2, -2, -2, 1, -1, 1, -1]
dy = [1, -1, 1, -1, 2, 2, -2, -2]

for tc in range(test_case):
    n = int(input())
    start_y, start_x = map(int, input().split())
    goal_y, goal_x = map(int, input().split())
    q = deque([[start_y, start_x, 0]])
    visit = [[False] * n for _ in range(n)]
    while q:
        y, x, cnt = q.popleft()
        if y == goal_y and x == goal_x:
            print(cnt)
            break
        visit[y][x] = True
        for t in range(8):
            ny, nx = y + dy[t], x + dx[t]
            if 0 <= ny < n and 0 <= nx < n and visit[ny][nx] == False:
                q.append([ny, nx, cnt+1])
                visit[ny][nx] = True