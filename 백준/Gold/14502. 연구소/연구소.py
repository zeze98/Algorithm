import copy
import sys
from collections import deque
input = sys.stdin.readline
sys.setrecursionlimit(100000)

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

dx = [1, 0, 0, -1]
dy = [0, 1, -1, 0]


def bfs():
    q = deque()
    temp = copy.deepcopy(board)

    for y in range(n):
        for x in range(m):
            if temp[y][x] == 2:
                q.append((y, x))

    while q:
        y, x = q.popleft()
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and temp[ny][nx] == 0:
                temp[ny][nx] = 2
                q.append((ny, nx))

    global answer
    cnt = 0

    for i in range(n):
        cnt += temp[i].count(0)

    answer = max(answer, cnt)


def wall(cnt):
    if cnt == 3:
        bfs()
        return

    for y in range(n):
        for x in range(m):
            if board[y][x] == 0:
                board[y][x] = 1
                wall(cnt+1)
                board[y][x] = 0


answer = 0
wall(0)
print(answer)
