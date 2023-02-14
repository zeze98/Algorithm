import sys

input = sys.stdin.readline


def dfs(i, j, idx, total):
    global ans
    if ans >= total + max_val * (3 - idx):
        return
    if idx == 3:
        ans = max(ans, total)
        return
    else:
        for t in range(4):
            ny = i + dy[t]
            nx = j + dx[t]
            if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == 0:
                if idx == 1:
                    visit[ny][nx] = 1
                    dfs(i, j, idx + 1, total + paper[ny][nx])
                    visit[ny][nx] = 0
                visit[ny][nx] = 1
                dfs(ny, nx, idx + 1, total + paper[ny][nx])
                visit[ny][nx] = 0


n, m = map(int, input().split())
paper = [list(map(int, input().split())) for _ in range(n)]
visit = [([0] * m) for _ in range(n)]
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
ans = 0
max_val = max(map(max, paper))

for i in range(n):
    for j in range(m):
        visit[i][j] = 1
        dfs(i, j, 0, paper[i][j])
        visit[i][j] = 0

print(ans)