import sys

input = sys.stdin.readline

n = int(input())
d = [0, 1, 1]
for i in range(3,91):
    answer = d[i-1] + d[i-2]
    d.append(answer)

print(d[n])