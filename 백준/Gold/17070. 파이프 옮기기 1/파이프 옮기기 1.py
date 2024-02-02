import sys

input = sys.stdin.readline

n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
dp = [[[0 for _ in range(3)] for _ in range(n)] for _ in range(n)]
# dp[y][x][가로, 세로, 대각선]
dp[0][1][0] = 1
for i in range(2, n):
    if board[0][i] == 0:
        dp[0][i][0] = dp[0][i-1][0]


for y in range(1, n):
    for x in range(1, n):
        # 대각선 체크
        if board[y][x] == 0 and board[y-1][x] == 0 and board[y][x-1] == 0:
            dp[y][x][2] = dp[y-1][x-1][0] + dp[y-1][x-1][1] + dp[y-1][x-1][2]

        if board[y][x] == 0:
            dp[y][x][0] = dp[y][x-1][0] + dp[y][x-1][2]
            dp[y][x][1] = dp[y-1][x][1] + dp[y-1][x][2]

print(sum(dp[n-1][n-1][i] for i in range(3)))
