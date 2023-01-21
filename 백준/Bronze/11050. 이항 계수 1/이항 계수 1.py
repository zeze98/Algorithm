import sys

input = sys.stdin.readline

N, K = map(int, input().split())

ans = 0
up = 1
d1 = 1
d2 = 1
for i in range(1, N+1):
    up *= i
for j in range(1,K+1):
    d1 *= j
for k in range(1,N-K+1):
    d2 *= k

ans = up / (d1 * d2)
print(int(ans))