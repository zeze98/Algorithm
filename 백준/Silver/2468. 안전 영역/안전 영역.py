import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

n = int(input())
low = 101
high = 0
board = []
for _ in range(n):
    temp = list(map(int, input().split()))
    x = max(temp)
    y = min(temp)
    high = max(high, x)
    low = min(low, y)
    board.append(temp)
answer = 1

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]


def check(x, y, rain):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] and board[nx][ny] > rain:
            visit[nx][ny] = False
            check(nx, ny, rain)


for rain in range(low, high):
    visit = [[True]*n for _ in range(n)]
    cnt = 0
    for x in range(n):
        for y in range(n):
            if board[x][y] > rain and visit[x][y]:
                cnt += 1
                visit[x][y] = False
                check(x, y, rain)
    answer = max(answer, cnt)

print(answer)
