import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()
ans = 0

if n == 1:
    check = 'IOI'
else:
    check = 'IOI' + 'OI' * (n - 1)

for i in range(m - len(check)):
    if s[i:i + len(check)] == check:
        ans += 1

print(ans)