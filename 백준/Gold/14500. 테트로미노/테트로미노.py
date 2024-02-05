import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, input().split())) for i in range(n)]
answer = 0
visit = [[True] * m for _ in range(n)]

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]


def dfs(y, x, point, cnt):
    global answer
    if answer >= point + max_board*(4-cnt):
        return
    if cnt == 4:
        answer = max(answer, point)
        return
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0 <= ny < n and 0 <= nx < m and visit[ny][nx]:
            if cnt == 2:
                visit[ny][nx] = False
                dfs(y, x, point + board[ny][nx], cnt + 1)
                visit[ny][nx] = True
            visit[ny][nx] = False
            dfs(ny, nx, point + board[ny][nx], cnt + 1)
            visit[ny][nx] = True


max_board = max(map(max, board))
for y in range(n):
    for x in range(m):
        visit[y][x] = False
        dfs(y, x, board[y][x], 1)
        visit[y][x] = True

print(answer)
