import sys

input = sys.stdin.readline

n = int(input())
board = list(map(int, input().split()))
maxdp = board
mindp = board

for _ in range(n-1):
    board = list(map(int, input().split()))
    maxdp = [board[0] + max(maxdp[0], maxdp[1]), board[1] +
             max(maxdp), board[2] + max(maxdp[1], maxdp[2])]
    mindp = [board[0] + min(mindp[0], mindp[1]), board[1] +
             min(mindp), board[2] + min(mindp[1], mindp[2])]

print(max(maxdp), min(mindp))
