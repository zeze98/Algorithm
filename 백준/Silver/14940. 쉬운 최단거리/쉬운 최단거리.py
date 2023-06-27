from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
board = []
q = deque([])
visit = [[False]*m for _ in range(n)]
rest = [[-1] * m for _ in range(n)]

"""
 1줄씩 입력 받을때 2의 위치를 찾고 찾은 2의 위치를 deque에 넣는다
 그후 2의 위치를 방문처리 하고 0으로 바꾼뒤
 입력받은 row를 보드에 넣는다
"""
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 2:
            q.append((i, j))
            visit[i][j] = True
            rest[i][j] = 0
            
        if row[j] == 0:
            rest[i][j] = 0
    board.append(row)

direc = [(1, 0), (-1, 0), (0, 1), (0, -1)]
while q:
    x, y = q.popleft()
    
    for dx, dy in direc:
        nx, ny = x + dx, y + dy
        
        if 0 <= nx < n and 0 <= ny < m and not visit[nx][ny] and board[nx][ny] == 1:
            q.append((nx,ny))
            visit[nx][ny] = True
            rest[nx][ny] = rest[x][y] + 1

for row in rest:
    for i in row:
        print(i, end = ' ')
    print()    