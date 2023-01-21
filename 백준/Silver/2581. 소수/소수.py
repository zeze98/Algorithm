m = int(input())
n = int(input())
answer = []
if m == 1:
    m = 2

for i in range(m, n+1):
    c = 0
    for j in range(2,i):
        if i % j == 0:
            c = 1
    if c == 0:
        answer.append(i)

if len(answer) == 0:
    print(-1)
else:
    answer.sort()
    print(sum(answer))
    print(answer[0])