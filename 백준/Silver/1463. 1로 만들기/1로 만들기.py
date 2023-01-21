import sys

input = sys.stdin.readline

T = int(input())
ans = [0]*(T + 1)

for i in range(2,T+1):
    ans[i] = ans[i-1] + 1
    if i % 3 == 0:
        ans[i] = min(ans[i], ans[i//3]+1)
    if i % 2 == 0:
        ans[i] = min(ans[i], ans[i//2]+1)

print(ans[T])