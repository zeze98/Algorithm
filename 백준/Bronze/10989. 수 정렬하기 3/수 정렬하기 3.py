import sys
input = sys.stdin.readline

N = int(input())
ans = [0] * 10001

for _ in range(N):
    ans[int(input())] += 1

for i in range(10001):
    if ans[i] != 0:
        for j in range(ans[i]):
            print(i)