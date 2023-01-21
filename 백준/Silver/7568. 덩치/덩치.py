import sys

input = sys.stdin.readline

N = int(input())
P = []

for _ in range(N):
    weight, height = map(int, input().split())
    P.append((weight, height))

for i in P:
    rank = 1
    for j in P:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1

    print(rank, end=' ')