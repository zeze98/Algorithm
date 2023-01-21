import sys

n = int(sys.stdin.readline())
for i in range(1,n+1):
    for b in range(n-i,0,-1):
        print(' ',end='')
    for s in range(1,i+1):
        print('*',end='')
    print()