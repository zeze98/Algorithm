from collections import deque


def solution(land):
    n = len(land)
    m = len(land[0])
    ans = [0 for _ in range(m)]
    visit = [[False for _ in range(m)] for _ in range(n)]

    def bfs(y, x, visit):
        q = deque([(y, x)])
        visit[y][x] = True
        cnt = 0
        dy = [1, 0, 0, -1]
        dx = [0, 1, -1, 0]
        minX, maxX = 501, 0
        while q:
            y, x = q.popleft()
            cnt += 1
            minX, maxX = min(minX, x), max(maxX, x)
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]

                if 0 <= ny < n and 0 <= nx < m and visit[ny][nx] == False and land[ny][nx] == 1:
                    q.append((ny, nx))
                    visit[ny][nx] = True

        for i in range(minX, maxX+1):
            ans[i] += cnt

    for y in range(n):
        for x in range(m):
            if visit[y][x] == False and land[y][x] == 1:
                bfs(y, x, visit)
    answer = max(ans)
    return answer