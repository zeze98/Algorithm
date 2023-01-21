import sys

n = list(map(int, sys.stdin.readline().split()))

ascen = sorted(n)
desc = sorted(n, reverse=True)
if n == ascen:
    print('ascending')
elif n == desc:
    print('descending')
else:
    print('mixed')