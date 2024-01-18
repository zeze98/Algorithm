import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
board = []
stack = deque()
answer = 0

for _ in range(n):
    board.append(list(map(int, input().split())))
stack.append((0, 0))

while stack:
    y, x = stack.popleft()
    if y == n-1 and x == n-1:
        answer = 1
        break
    move = board[y][x]
    if move == 0:
        continue
    if move + y < n:
        stack.append((y + move, x))
    if move + x < n:
        stack.append((y, x + move))

if answer == 1:
    print('HaruHaru')
else:
    print('Hing')
