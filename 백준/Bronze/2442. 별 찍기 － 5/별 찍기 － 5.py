import sys

input = sys.stdin.readline()

n = int(input)
s = 1
b = n - 1
for i in range(n):
    print(' '*(b-i)+'*'*s)
    s += 2