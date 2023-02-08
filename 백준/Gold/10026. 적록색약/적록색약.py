import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
pic = [list(map(str,input().rstrip())) for _ in range(n)]
normal = [0, 0, 0]
rgc = [0, 0]


def n_dfs(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    color = pic[y][x]
    pic[y][x] = color.lower()
    for t in range(4):
        nx = x + dx[t]
        ny = y + dy[t]
        if 0 <= nx < n and 0 <= ny < n and pic[ny][nx] == color:
            n_dfs(ny, nx)


def dfs(y, x):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    color = pic[y][x]
    pic[y][x] = 0
    if color == 'r' or color == 'g':
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < n:
                if pic[ny][nx] == 'r' or pic[ny][nx] == 'g':
                    dfs(ny, nx)
    elif color == 'b':
        for t in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            if 0 <= nx < n and 0 <= ny < n and pic[ny][nx] == color:
                dfs(ny, nx)


for i in range(n):
    for j in range(n):
        if pic[i][j] == 'R':
            n_dfs(i, j)
            normal[0] += 1
        elif pic[i][j] == 'G':
            n_dfs(i, j)
            normal[1] += 1
        elif pic[i][j] == 'B':
            n_dfs(i, j)
            normal[2] += 1
print(sum(normal), end=' ')

for q in range(n):
    for p in range(n):
        if pic[q][p] == 'r':
            dfs(q, p)
            rgc[0] += 1
        elif pic[q][p] == 'g':
            dfs(q, p)
            rgc[0] += 1
        elif pic[q][p] == 'b':
            dfs(q, p)
            rgc[1] += 1
print(sum(rgc))
