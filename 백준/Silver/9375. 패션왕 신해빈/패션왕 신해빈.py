import collections
import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    n = int(input())
    closet = []
    for i in range(n):
        x, y = input().split()
        closet.append(y)
    num = 1
    ans = collections.Counter(closet)

    for key in ans:
        num *= ans[key] + 1
    print(num-1)