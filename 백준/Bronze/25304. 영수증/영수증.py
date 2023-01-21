import sys

X = int(sys.stdin.readline())
N = int(sys.stdin.readline())
price_sum = 0

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    price_sum += a*b

if price_sum == X:
    print('Yes')
else:
    print('No')