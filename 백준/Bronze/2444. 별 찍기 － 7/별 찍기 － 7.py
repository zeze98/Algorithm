n = int(input())
for i in range(1, n):
    print(' '*(n-i)+'*'*(1+(i-1)*2))
for j in range(n, 0, -1):
    print(' '*(n-j)+'*'*(1+(j-1)*2))