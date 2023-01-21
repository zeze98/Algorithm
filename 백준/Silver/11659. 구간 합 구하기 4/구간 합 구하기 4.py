import sys

input = sys.stdin.readline

N, M = map(int, input().split())
listN = list(map(int, input().split()))
sumlistN = [0]
t = 0
for x in listN:
    t += x
    sumlistN.append(t)

for _ in range(M):
    i, j = map(int, input().split())
    print(sumlistN[j]-sumlistN[i-1])