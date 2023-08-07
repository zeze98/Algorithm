import sys
from collections import deque

input = sys.stdin.readline

n, k = map(int, input().split())
q = deque()
q.append([n, 0])
visited = [0] * 100001

while True:
    s = q.popleft()
    now = s[0]
    second = s[1]

    if now == k:
        print(second)
        break

    if now * 2 <= 100000 and visited[now * 2] == 0:
        visited[now * 2] = 1
        q.appendleft([now * 2, second])
    if now - 1 >= 0 and visited[now - 1] == 0:
        visited[now - 1] = 1
        q.append([now - 1, second + 1])
    if now + 1 <= 100000 and visited[now + 1] == 0:
        visited[now + 1] == 1
        q.append([now + 1, second + 1])
