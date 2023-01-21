n = int(input())
ns = 1

def fac(n):
    if n == 0:
        ns = 1
        print(ns)
    else:
        ns = 1
        for i in range(n,1,-1):
            ns = ns * i
        print(ns)
fac(n)