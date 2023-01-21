n = list(map(int, input().split()))
n.sort()
if len(set(n)) == 1:
    print(10000+n[0]*1000)
elif n[0] == n[1] or n[1] == n[2]:
    print(1000 + n[1]*100)
else:
    print(n[2]*100)