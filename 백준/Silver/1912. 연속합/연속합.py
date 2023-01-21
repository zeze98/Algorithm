import sys

read = sys.stdin.readline

n = int(read())
listn = list(map(int, read().split()))

for i in range(1,n):
    listn[i] = max(listn[i], listn[i]+listn[i-1])

print(max(listn))