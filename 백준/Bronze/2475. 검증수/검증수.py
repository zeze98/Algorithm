import sys

input = sys.stdin.readline

num = list(map(int, input().split()))
ans = 0

for i in range(len(num)):
    ans += num[i]*num[i]

print(ans % 10)