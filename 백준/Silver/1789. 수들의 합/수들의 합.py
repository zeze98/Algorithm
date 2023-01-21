S = int(input())
start = 1
target = 0
N = 0

while target < S:
    target += start
    start += 1
    N += 1
    if (start + target) > S:
        break

print(N)