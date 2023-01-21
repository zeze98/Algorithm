import sys

input = sys.stdin.readline

N = int(input())
Steps = [0] + [int(input()) for _ in range(N)]
dp = [0] * (N+1)

if N >= 1:
    dp[1] = Steps[1]
if N >= 2:
    dp[2] = Steps[1] + Steps[2]
if N >= 3:
    for i in range(3, N+1):
        dp[i] = max(dp[i-3] + Steps[i-1]+Steps[i], dp[i-2]+Steps[i])

print(dp[N])