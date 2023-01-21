import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N = int(input())
    def dp(N):
        d = [0] * 12
        d[0] = 0
        d[1] = 1
        d[2] = 2
        d[3] = 4

        for i in range(4,N+1):
            d[i] = d[i-1] + d[i-2] + d[i-3]
        return d[N]
    print(dp(N))