import sys

input = sys.stdin.readline

S = input().rstrip().split('-')

n = []
for i in S:
    cnt = 0
    x = i.split('+')
    for j in x:
        cnt += int(j)
    n.append(cnt)
num = n[0]
for k in range(1,len(n)):
    num -= n[k]
print(num)