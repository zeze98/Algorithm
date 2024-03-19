from collections import deque


def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    maxX, maxY = 0, 0
    for lx, ly, rx, ry in rectangle:
        maxX = max(rx * 2, maxX)
        maxY = max(ry * 2, maxY)
    board = [[0] * (maxX + 2) for _ in range(maxY + 2)]

    # 내부 채우기 과정
    for lx, ly, rx, ry in rectangle:
        for x in range((lx * 2), (rx * 2) + 1):
            for y in range((ly * 2), (ry * 2) + 1):
                board[y][x] = 2

    # 테두리 판별 과정
    tdy = [1, 0, 0, -1, 1, 1, -1, -1]
    tdx = [0, 1, -1, 0, 1, -1, 1, -1]
    for y in range(1, maxY + 1):
        for x in range(1, maxX + 1):
            for t in range(8):
                ty = y + tdy[t]
                tx = x + tdx[t]
                if board[ty][tx] == 0 and board[y][x] == 2:
                    board[y][x] = 1
                    break

    dy = [1, 0, 0, -1]
    dx = [0, 1, -1, 0]
    q = deque([(characterX * 2, characterY * 2, 0)])
    itemX *= 2
    itemY *= 2
    while q:
        cx, cy, cnt = q.popleft()
        board[cy][cx] = 2
        if cx == itemX and cy == itemY:
            answer = (cnt // 2)
            break

        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            if board[ny][nx] == 1:
                q.append((nx, ny, cnt + 1))

    return answer