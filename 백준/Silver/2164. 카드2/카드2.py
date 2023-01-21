import sys

n = int(sys.stdin.readline())
square = 2

while True:
    if (n == 1 or n==2):
        print(n)
        break
    square *= 2
    if square >= n:
        print((n - (square // 2))*2)
        break