import sys

n = int(sys.stdin.readline())

for i in range(n,0,-1):
    for j in range(0,i):
        print('*',end='')
    print()