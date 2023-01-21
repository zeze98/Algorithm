n = int(input())
ln = 1000 - n
coin = [500, 100, 50, 10, 5, 1]
answer = 0

for i in coin:
    answer += ln // i
    ln = ln%i
print(answer)