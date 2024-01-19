import sys

input = sys.stdin.readline

board = [list(map(int, input().split())) for _ in range(5)]
visit = [[True] * 5 for _ in range(5)]
r, c = map(int, input().split())
dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]


def dfs(r, c, apple, chance):
    visit[r][c] = False
    if board[r][c] == 1:
        apple += 1
    if apple >= 2:
        return 1
    if chance <= 0:
        visit[r][c] = True
        return 0
    for i in range(4):
        ny = r + dy[i]
        nx = c + dx[i]
        if 0 <= ny < 5 and 0 <= nx < 5:
            if visit[ny][nx] and board[ny][nx] != -1:
                if dfs(ny, nx, apple, chance - 1) == 1:
                    return 1
    visit[r][c] = True
    return 0


print(dfs(r, c, 0, 3))
