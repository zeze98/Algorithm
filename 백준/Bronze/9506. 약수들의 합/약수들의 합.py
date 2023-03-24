import sys

input = sys.stdin.readline

while True:
    x = int(input())
    ans = []
    if x == -1:
        break

    for i in range(1, x):
        if x % i == 0:
            ans.append(i)
    if sum(ans) == x:
        print(x, '=', end=' ')
        for i in range(len(ans)-1):
            print(ans[i], end=' + ')
        print(ans[-1])
    else:
        print(x, 'is NOT perfect.')