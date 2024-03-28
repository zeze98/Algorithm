from collections import deque
import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = deque(list(map(int, input().split())))

answer = 0
belt = deque([False] * n)
while True:
    answer += 1
    a.rotate(1)
    belt.rotate(1)
    belt[n-1] = False

    for i in range(n-2, -1, -1):
        if belt[i] and not belt[i+1] and a[i + 1] > 0:
            belt[i], belt[i+1] = False, True
            a[i+1] -= 1

    belt[n-1] = False

    if a[0] > 0:
        belt[0] = True
        a[0] -= 1
    if a.count(0) >= k:
        print(answer)
        break