n = int(input())
num = []
for i in range(n):
    num.append(int(input()))
num = sorted(num)
for j in range(n):
    print(num[j])