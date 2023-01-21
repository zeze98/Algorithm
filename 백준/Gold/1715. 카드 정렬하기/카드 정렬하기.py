import heapq
import sys

N = int(sys.stdin.readline())
card = []
for i in range(N):
    heapq.heappush(card, int(sys.stdin.readline()))

ans = 0
while len(card) != 1:
    n1 = heapq.heappop(card)
    n2 = heapq.heappop(card)
    Sum = n1 + n2
    ans += Sum
    heapq.heappush(card, Sum)

print(ans)