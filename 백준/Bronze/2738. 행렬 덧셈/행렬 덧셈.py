import sys

input = sys.stdin.readline

N, M = map(int, input().split())
A = []
B = []

for _ in range(N):
    AN = list(map(int, input().split()))
    A.append(AN)

for _ in range(N):
    BN = list(map(int, input().split()))
    B.append(BN)

for i in range(N):
    for j in range(M):
        A[i][j] = A[i][j] + B[i][j]

for x in range(N):
    for y in range(M):
        print(A[x][y], end=' ')
    print()