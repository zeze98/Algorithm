import sys

input = sys.stdin.readline

a = input().rstrip()
b = input().rstrip()
num = ''
# 초기 시작 번호 만들기
for i in range(len(a)):
    num += a[i] + b[i]

while len(num) > 2:
    temp = ''
    for i in range(len(num)-1):
        n = (int(num[i]) + int(num[i+1])) % 10
        temp += str(n)
    num = temp
print(num)