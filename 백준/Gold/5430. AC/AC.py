import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    p = input().rstrip()
    n = int(input())
    array = deque(input().rstrip()[1:-1].split(','))
    check = 0
    r, f = 0, 0

    if n == 0:
        array = deque()
        f = 0

    for i in p:
        if i == 'R':
            r += 1
        elif i == 'D':
            if len(array) < 1:
                check += 1
                print("error")
                break
            else:
                if r % 2 == 0:
                    array.popleft()
                else:
                    array.pop()

    if check == 0:
        if r % 2 == 0:
            print('[' + ','.join(array) + ']')
        else:
            array.reverse()
            print('[' + ','.join(array) + ']')
