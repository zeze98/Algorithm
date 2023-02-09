import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())
board = [0] * 101
visit = [False] * 101

ladder = dict()
snake = dict()

for _ in range(n):
    ladder_start, ladder_end = map(int, input().split())
    ladder[ladder_start] = ladder_end
for _ in range(m):
    snake_start, snake_end = map(int, input().split())
    snake[snake_start] = snake_end


def bfs():
    q = deque([1])
    visit[1] = True
    while q:
        now = q.popleft()
        for dice in range(1, 7):
            check_board = now + dice
            if 0 < check_board <= 100 and not visit[check_board]:
                if check_board in ladder.keys():
                    check_board = ladder[check_board]
                if check_board in snake.keys():
                    check_board = snake[check_board]
                if not visit[check_board]:
                    q.append(check_board)
                    visit[check_board] = True
                    board[check_board] = board[now] + 1


bfs()

print(board[100])