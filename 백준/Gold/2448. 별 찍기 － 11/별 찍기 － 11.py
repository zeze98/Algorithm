import sys

input = sys.stdin.readline

n = int(input())
total = [[' '] * 2 * n for _ in range(n)]


def divis(i, j, size):
    if size == 3:
        total[i][j] = '*'
        total[i + 1][j - 1] = '*'
        total[i + 1][j + 1] = '*'
        for t in range(-2, 3):
            total[i + 2][j - t] = '*'
    else:
        nsize = size // 2
        divis(i, j, nsize)
        divis(i + nsize, j - nsize, nsize)
        divis(i + nsize, j + nsize, nsize)


divis(0, n-1, n)
for tot in total:
    print("".join(tot))
