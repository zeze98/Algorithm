import sys

n = int(sys.stdin.readline())

cnt = 1
beeroom = 1
while n > beeroom:
    beeroom += 6 * cnt
    cnt += 1

print(cnt)