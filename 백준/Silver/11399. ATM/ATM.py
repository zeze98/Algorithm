n = int(input())
time = list(map(int, input().split()))
time = sorted(time)
total_time = 0
for i in range(n+1):
    for j in range(i):
        total_time += time[j]
        
print(total_time)