import sys
input = sys.stdin.readline

n, m = map(int, input().split())
answer = 0
visit = [[True] * m for _ in range(n)]
room = []
for _ in range(n):
    room.append(input().strip())


def check(y, x, type):
    if visit[y][x] == True and type == '-' and room[y][x] == type:
        visit[y][x] = False
        if x < m-1:
            check(y, x+1, type)
    if visit[y][x] == True and type == '|' and room[y][x] == type:
        visit[y][x] = False
        if y < n-1:
            check(y+1, x, type)


for y in range(n):
    for x in range(m):
        if room[y][x] == '-' and visit[y][x] == True:
            visit[y][x] = False
            if x < m-1:
                check(y, x+1, '-')
            answer += 1

        if room[y][x] == '|' and visit[y][x] == True:
            visit[y][x] = False
            if y < n-1:
                check(y+1, x, '|')
            answer += 1

print(answer)