import sys

input = sys.stdin.readline

n = int(input())
g = []
for _ in range(n):
    g.append(list(map(int, input().split())))

for k in range(n):
    for i in range(n):
        for j in range(n):
            if g[i][j] == 1 or (g[i][k] == 1 and g[k][j] == 1):
                g[i][j] = 1


for row in g:
    for col in row:
        print(col, end=" ")
    print()