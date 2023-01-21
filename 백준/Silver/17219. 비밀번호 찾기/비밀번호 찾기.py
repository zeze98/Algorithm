import sys

input = sys.stdin.readline

N, M = map(int, input().split())
sitedic = {}
findsite = []

for i in range(N):
    key, val = map(str, input().split())
    sitedic[key] = val

for j in range(M):
    findsite.append(input().rstrip())

for x in range(M):
    print(sitedic[findsite[x]])