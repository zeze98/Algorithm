import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = []
for i in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)

dp = [[0]*(n+1) for _ in range(n+1)]

for x in range(1, n+1):
    for y in range(1, n+1):
        dp[x][y] = dp[x][y-1] + dp[x-1][y] - dp[x-1][y-1] + arr[x-1][y-1]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    ans = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(ans)