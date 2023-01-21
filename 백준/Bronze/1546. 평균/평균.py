N = int(input())
num = list(map(int, input().split()))
M = max(num)
avg = 0
for i in range(N):
    num[i] = num[i] / M * 100
for i in range(N):
    avg += num[i]
print(round(avg/N, 6))