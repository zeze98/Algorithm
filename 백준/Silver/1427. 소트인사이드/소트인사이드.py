n = input()
ns = []
lenn = len(n)
for i in range(lenn):
    x = int(n)%10
    ns.append(x)
    n = int(n)/10
ns.sort(reverse=True)

for i in range(lenn):
    print(ns[i],end='')