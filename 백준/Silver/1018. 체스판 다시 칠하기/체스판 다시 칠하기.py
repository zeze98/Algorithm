import sys

input = sys.stdin.readline

N, M = map(int, input().split())
chess = []
repair = []

for _ in range(N):
    chess.append(input().rstrip())

for x in range(N-7):
    for y in range(M-7):
        indexx = 0
        indexy = 0
        for i in range(x, x+8):
            for j in range(y, y+8):
                if (i + j) % 2 == 0:
                    if chess[i][j] != 'W':
                        indexx += 1
                    if chess[i][j] != 'B':
                        indexy += 1
                else:
                    if chess[i][j] != 'B':
                        indexx += 1
                    if chess[i][j] != 'W':
                        indexy += 1
        repair.append(min(indexx, indexy))

print(min(repair))