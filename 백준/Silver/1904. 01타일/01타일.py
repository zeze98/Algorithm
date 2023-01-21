import sys

input = sys.stdin.readline

dp = [0] * 1000001
dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 3
dp[4] = 5

N = int(input())

if N >= 5:
    for t in range(5,N+1):
        dp[t] = dp[t-1]%15746 + dp[t-2]%15746

print(dp[N]%15746)