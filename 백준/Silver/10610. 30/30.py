import sys
ip = sys.stdin.readline()

N = int(ip)
num = []
answer = 0
for i in str(N):
    num.append(int(i))
num.sort(reverse=True)
if sum(num) % 3 != 0:
    print(-1)
else:
    if num[len(num)-1] != 0:
        print(-1)
    else:
        print(*num,sep='')