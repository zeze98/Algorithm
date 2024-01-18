import sys
from collections import deque
input = sys.stdin.readline

a, k = map(int, input().split())
answer = 0
while True:
    if a == k:
        print(answer)
        break
    if k % 2 == 0 and k >= a*2:
        k = int(k/2)
    else:
        k -= 1
    answer += 1
