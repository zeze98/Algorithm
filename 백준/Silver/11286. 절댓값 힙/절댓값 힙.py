import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = []


for _ in range(N):
    x = int(input())
    if x == 0:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])

    else:
        if x < 0:
            heapq.heappush(arr,(-x, x))
        else:
            heapq.heappush(arr,(x,x))