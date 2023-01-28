import sys
import heapq

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    k = int(input())
    max_q, min_q = [], []
    visit = [False] * k

    for j in range(k):
        command, n = input().split()

        if command == 'I':
            heapq.heappush(max_q, (int(n), j))
            heapq.heappush(min_q, (-int(n), j))
            visit[j] = True

        else:
            if n == '1':
                while min_q and not visit[min_q[0][1]]:
                    heapq.heappop(min_q)
                if min_q:
                    visit[min_q[0][1]] = False
                    heapq.heappop(min_q)
            else:
                while max_q and not visit[max_q[0][1]]:
                    heapq.heappop(max_q)
                if max_q:
                    visit[max_q[0][1]] = False
                    heapq.heappop(max_q)

    while max_q and not visit[max_q[0][1]]:
        heapq.heappop(max_q)
    while min_q and not visit[min_q[0][1]]:
        heapq.heappop(min_q)

    if not max_q or not min_q:
        print("EMPTY")
    else:
        a = -min_q[0][0]
        b = max_q[0][0]
        print("%d %d" % (a, b))