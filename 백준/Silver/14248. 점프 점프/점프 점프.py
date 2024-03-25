from collections import deque
import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
s = int(input())
visit = [0] * n

q = deque([s-1])
while q:
    stone = q.popleft()
    visit[stone] = 1
    move = a[stone]
    if 0 <= stone + move < n and visit[stone + move] == 0:
        q.append(stone + move)
        visit[stone + move] = 1
    if 0 <= stone - move < n and visit[stone - move] == 0:
        q.append(stone - move)
        visit[stone - move] = 1

print(sum(visit))
