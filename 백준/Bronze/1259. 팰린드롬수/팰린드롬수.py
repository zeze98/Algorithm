import sys

answer = []
while True:
    n = sys.stdin.readline().strip()
    if n == '0':
        break

    if n == n[::-1]:
        answer.append('yes')
    else:
        answer.append('no')

for i in range(len(answer)):
    print(answer[i])