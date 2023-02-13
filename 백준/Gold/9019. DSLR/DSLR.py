import sys
from collections import deque

input = sys.stdin.readline

for _ in range(int(input())):
    a, b = map(int, input().split())
    q = deque()
    q.append((a, ""))
    visit = [False] * 10000

    while q:
        n, path = q.popleft()
        visit[n] = True
        if n == b:
            print(path)
            break

        check_n = (2 * n) % 10000
        if not visit[check_n]:
            q.append((check_n, path+"D"))
            visit[check_n] = True

        check_n = (n - 1) % 10000
        if not visit[check_n]:
            q.append((check_n, path+"S"))
            visit[check_n] = True

        check_n = (10 * n + (n // 1000)) % 10000
        if not visit[check_n]:
            q.append((check_n, path+"L"))
            visit[check_n] = True

        check_n = (n // 10 + (n % 10) * 1000) % 10000
        if not visit[check_n]:
            q.append((check_n, path+"R"))
            visit[check_n] = True