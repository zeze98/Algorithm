import sys

input = sys.stdin.readline

n, k = map(int, input().split())
answer = [[0 for _ in range(k+1)] for _ in range(n+1)]
stuff = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    w, v = stuff[i][0], stuff[i][1]
    for carry in range(1, k+1):
        if carry < w:
            answer[i+1][carry] = answer[i][carry]
        else:
            answer[i+1][carry] = max(answer[i][carry],
                                     answer[i][carry - w] + v)

print(answer[-1][k])
