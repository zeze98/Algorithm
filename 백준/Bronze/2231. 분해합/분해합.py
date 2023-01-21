import sys

input = sys.stdin.readline

N = int(input())
ans = 0

for i in range(1,N+1):
    A = list(map(int, str(i)))
    ans = i + sum(A)
    if ans == N:
        print(i)
        break
    if i == N:
        print(0)