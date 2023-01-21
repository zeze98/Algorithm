import sys

k = int(input())
nums = []
for i in range(k):
    n = int(sys.stdin.readline())
    if n == 0:
        nums.pop()
    else:
        nums.append(n)

print(sum(nums))