import sys
import heapq

input = sys.stdin.readline

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
cost = [1e9 for _ in range(n+1)]
for _ in range(m):
    s, e, c = map(int, input().split())
    graph[s].append([e, c])
start, end = map(int, input().split())
heap = []
cost[start] = 0
heapq.heappush(heap, [0, start])

while heap:
    c, p = heapq.heappop(heap)
    if cost[p] < c:
        continue
    for next_point, next_cost in graph[p]:
        sum_cost = c + next_cost
        if sum_cost >= cost[next_point]:
            continue

        cost[next_point] = sum_cost
        heapq.heappush(heap, [sum_cost, next_point])

print(cost[end])
