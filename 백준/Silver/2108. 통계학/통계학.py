import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
num = []
for i in range(N):
    num.append(int(input()))
num.sort()

print(int(round(sum(num)/N, 0)))
print(num[N//2])

c = Counter(num)
b = c.most_common()
if len(num) > 1:
    if b[0][1] == b[1][1]:
        print(b[1][0])
    else:
        print(b[0][0])
else:
    print(num[0])

print(num[-1] - num[0])