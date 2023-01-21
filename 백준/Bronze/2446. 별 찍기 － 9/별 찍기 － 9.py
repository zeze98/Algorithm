import sys

input = sys.stdin.readline()

n = int(input)

for i in range(n):
    print(' '*i+'*'*(2*(n-i)-1))
for j in range(1,n):
    print(' '*(2*n-1-n-j)+'*'*(2*(j+1)-1))