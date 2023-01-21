import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int, input().split())
ans = []
circleQ = deque()
for i in range(1, N+1):
    circleQ.append(i)

while circleQ:
    for i in range(K-1):
        circleQ.append(circleQ.popleft())
    ans.append(circleQ.popleft())

print('<', end='')
for i in range(len(ans)-1):
    print(ans[i], end=', ')
print(ans[-1], end='')
print('>', end='')