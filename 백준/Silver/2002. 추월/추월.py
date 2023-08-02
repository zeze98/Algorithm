import sys

input = sys.stdin.readline

n = int(input())
daegun = {}
youngsik = []
answer = 0
for i in range(n):
    car = input().rstrip()
    daegun[car] = i

for _ in range(n):
    car = input().rstrip()
    youngsik.append(car)


for i in range(n-1):
    for j in range(i + 1, n):
        if daegun[youngsik[i]] > daegun[youngsik[j]]:
            answer += 1
            break

print(answer)