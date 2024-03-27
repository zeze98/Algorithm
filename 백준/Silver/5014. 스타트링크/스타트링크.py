from collections import deque
import sys

input = sys.stdin.readline

f, s, g, u, d = map(int, input().split())
# f 는 총 층수, s 는 강호 시작, g 목적지
tower = deque([(s, 0)])


def elevator(f, s, g, u, d, tower):
    visit = [0] * f
    while tower:
        now, cnt = tower.popleft()
        visit[now-1] = 1
        if now == g:
            return print(cnt)
        up, down = now + u, now - d
        if 0 < up <= f and visit[up-1] == 0:
            tower.append([up, cnt + 1])
            visit[up-1] = 1
        if 0 < down <= f and visit[down-1] == 0:
            tower.append([down, cnt + 1])
            visit[down-1] = 1

    return print('use the stairs')


def check(f, s, g, u, d, tower):
    if s > g and d == 0:
        return print('use the stairs')
    if s < g and u == 0:
        return print('use the stairs')
    else:
        return elevator(f, s, g, u, d, tower)


check(f, s, g, u, d, tower)
