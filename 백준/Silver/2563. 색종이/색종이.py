import sys

input = sys.stdin.readline

n = int(input())
white = [[0]*100 for _ in range(100)]
answer = 0
for i in range(n):
    x, y = map(int, input().split())
    for dx in range(x, x+10):
        for dy in range(y, y+10):
            if white[dy][dx] == 0:
                answer +=1
                white[dy][dx] = 1
            elif white[dy][dx] == 1:
                continue
print(answer)