import sys
from collections import deque
input = sys.stdin.readline

gear = [deque(list(map(int, input().rstrip()))) for _ in range(4)]
k = int(input())

for _ in range(k):
    connection = []
    for i in range(4):
        connection.append([gear[i][6], gear[i][2]])
    n, d = map(int, input().split())
    n = n-1

    if n != 0:
        for i in range(n, 0, -1):
            if connection[i][0] != connection[i-1][1]:
                if (n-(i-1)) % 2 == 0:
                    gear[i-1].rotate(d)
                elif (n-(i-1)) % 2 != 0:
                    gear[i-1].rotate(-1*d)
            elif connection[i][0] == connection[i-1][1]:
                break

    if n != 3:
        for i in range(n, 3):
            if connection[i][1] != connection[i+1][0]:
                if (n-(i+1)) % 2 == 0:
                    gear[i+1].rotate(d)
                elif (n-(i+1)) % 2 != 0:
                    gear[i+1].rotate(-1*d)
            elif connection[i][1] == connection[i+1][0]:
                break
    gear[n].rotate(d)

answer = 0
if gear[0][0] == 1:
    answer += 1
if gear[1][0] == 1:
    answer += 2
if gear[2][0] == 1:
    answer += 4
if gear[3][0] == 1:
    answer += 8
print(answer)
