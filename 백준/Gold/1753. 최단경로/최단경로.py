import sys
import heapq
input = sys.stdin.readline

# 정점의 갯수 v, 간선의 갯수 e
v, e = map(int, input().split())
# 시작점 k
k = int(input())
graph = [[]*(v+1) for _ in range(v+1)]
answer = [1e9] * (v+1)

for _ in range(e):
    # 시작점, 끝점, 가중치
    start, end, w = map(int, input().split())
    graph[start].append((end, w))


def check(st_po):
    q = []
    heapq.heappush(q, (0, st_po))
    answer[st_po] = 0
    while q:
        dist, now = heapq.heappop(q)
        if answer[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < answer[i[0]]:
                answer[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))


check(k)

for i in range(1, v+1):
    if answer[i] == 1e9:
        print('INF')
    else:
        print(answer[i])
