import sys

input = sys.stdin.readline

n = int(input())

dot = [list(map(int, input().rstrip())) for _ in range(n)]


def squeeze(x, y, n):
    check = dot[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != dot[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n//2
        squeeze(x, y, n)
        squeeze(x, y+n, n)
        squeeze(x+n, y, n)
        squeeze(x+n, y+n, n)
        print(")", end='')
    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')


squeeze(0, 0, n)
