from collections import deque
import sys

input = sys.stdin.readline

dz = [1, -1, 0, 0, 0, 0]
dx = [0, 0, 1, -1, 0, 0]
dy = [0, 0, 0, 0, 1, -1]

while True:
    l, r, c = map(int, input().split())
    if l == 0 and r == 0 and c == 0:
        break
    building = []
    visit = [[[False]*c for _ in range(r)] for _ in range(l)]
    q = deque()
    for floor in range(l):
        building.append([list(input().strip()) for _ in range(r)])
        temp = input()
    answer = False

    for z in range(l):
        for y in range(r):
            for x in range(c):
                if building[z][y][x] == 'S':
                    start = (z, y, x, 0)
                    visit[z][y][x] = True
                if building[z][y][x] == 'E':
                    goal = (z, y, x)

    q.append(start)
    while q:
        z, y, x, cnt = q.popleft()
        if (z, y, x) == goal:
            answer = True
            print(f'Escaped in {cnt} minute(s).')
            break

        for t in range(6):
            nz, ny, nx = z + dz[t], y + dy[t], x + dx[t]
            if 0 <= nz < l and 0 <= ny < r and 0 <= nx < c and visit[nz][ny][nx] == False:
                if building[nz][ny][nx] != '#':
                    q.append((nz, ny, nx, cnt + 1))
                    visit[nz][ny][nx] = True

    if answer == False:
        print('Trapped!')
