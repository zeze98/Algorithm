from collections import deque
import sys


input = sys.stdin.readline

n, K = map(int, input().split())

max_N = 100000
visit = [0] * (max_N+1)

def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == K:
            print(visit[x])
            break
        for i in (x-1, x+1, x*2):
            if 0 <= i <= max_N and not visit[i]:
                visit[i] = visit[x] + 1
                q.append(i)


bfs()