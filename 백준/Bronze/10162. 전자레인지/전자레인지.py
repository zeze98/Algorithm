import sys

input = sys.stdin.readline()

T = int(input)
answer = []
button = [300, 60, 10]

for i in button:
    answer.append(T // i)
    T %= i

if T != 0:
    answer = -1
    print(answer)
else:
    print(*answer, sep=' ')