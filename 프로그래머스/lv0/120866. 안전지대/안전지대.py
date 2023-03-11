from collections import deque

def solution(board):
    answer = 0
    dx = [-1, 1, 0, 0, 1, 1, -1, -1]
    dy = [0, 0, -1, 1, -1, 1, 1, -1]
    n = len(board)
    visit = [[False] * n for _ in range(n)]
    def bfs(x, y):
        q = deque()
        q.append((x,y))
        while q:
            a, b = q.popleft()
            visit[a][b] = True
            for i in range(8):
                nx = dx[i] + a
                ny = dy[i] + b
                if 0 <= nx < n and 0 <= ny < n and not visit[nx][ny]:
                    if board[nx][ny] == 1:
                        q.append((nx, ny))
                    else:
                        board[nx][ny] = 2

    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:
                bfs(i,j)
    for i in range(n):
        answer += board[i].count(0)
    return answer