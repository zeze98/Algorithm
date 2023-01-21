n, k = map(int,input().split())
coin = []
cnt = 0
for i in range(n):
    coin.append(int(input()))
coin.sort(reverse=True)
for i in coin:
    cnt += k // i
    k %= i

print(cnt)