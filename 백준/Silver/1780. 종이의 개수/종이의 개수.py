import sys

input = sys.stdin.readline

N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

ans = []


def check(x, y, N):
    color = paper[x][y]
    for i in range(x, x + N):
        for j in range(y, y + N):
            if color != paper[i][j]:
                check(x, y, N // 3)
                check(x, y + N // 3, N // 3)
                check(x, y + N // 3 + N // 3, N // 3)
                check(x + N // 3, y, N // 3)
                check(x + N // 3 + N // 3, y, N // 3)
                check(x + N // 3, y + N // 3, N // 3)
                check(x + N // 3 + N // 3, y + N // 3, N // 3)
                check(x + N // 3, y + N // 3 + N // 3, N // 3)
                check(x + N // 3 + N // 3, y + N // 3 + N // 3, N // 3)
                return
    if color == 0:
        ans.append(0)
    elif color == 1:
        ans.append(1)
    elif color == -1:
        ans.append(-1)


check(0, 0, N)
print(ans.count(-1))
print(ans.count(0))
print(ans.count(1))