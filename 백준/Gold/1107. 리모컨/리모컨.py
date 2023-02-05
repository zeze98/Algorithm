import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
button = [i for i in range(9, -1, -1)]
ans = abs(100 - n)

if m > 0:
    error_button = list(map(int, input().split()))
    for i in error_button:
        button.remove(i)
if n == 100:
    print(0)
else:
    for num in range(1000001):
        num = str(num)
        for x in range(len(num)):
            if int(num[x]) not in button:
                break
            elif x == len(num) - 1:
                ans = min(ans, abs(int(num) - n) + len(num))
    print(ans)