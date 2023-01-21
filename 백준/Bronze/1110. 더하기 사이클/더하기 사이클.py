import sys

n = int(sys.stdin.readline())
dn = n
cn = 0
l = 0
if n == 0:
    l += 1
while cn != n:
    n1 = dn//10 + dn%10
    if n1>=10:
        n1 = n1%10
    cn = (dn%10)*10 + n1
    dn = cn
    l += 1

print(l)