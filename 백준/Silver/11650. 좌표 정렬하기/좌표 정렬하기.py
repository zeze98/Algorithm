n = int(input())
loc = []
for i in range(n):
    loc.append(list(map(int, input().split())))
loc.sort()
for i in range(n):
    print(*loc[i])