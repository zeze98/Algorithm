import sys

input = sys.stdin.readline()

n = int(input)
for i in range(1,n+1):
    print(' '*(n-i) + '*'*i)
for j in range(1,n):
    print(' '*j + '*'*(n-j))