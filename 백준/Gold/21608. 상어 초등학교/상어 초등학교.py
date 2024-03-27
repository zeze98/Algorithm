import sys

input = sys.stdin.readline

n = int(input())
room = [[0] * n for _ in range(n)]
students = {}
for _ in range(n*n):
    student_n, like_1, like_2, like_3, like_4 = map(int, input().split())
    students[student_n] = [like_1, like_2, like_3, like_4]

dy = [1, 0, 0, -1]
dx = [0, 1, -1, 0]


def calculate(room):
    answer = 0
    for y in range(n):
        for x in range(n):
            cnt = 0
            student = room[y][x]
            want = students[student]
            for t in range(4):
                ny, nx = y + dy[t], x + dx[t]
                if 0 <= ny < n and 0 <= nx < n and room[ny][nx] in want:
                    cnt += 1
            if cnt == 0:
                answer += 0
            elif cnt == 1:
                answer += 1
            elif cnt == 2:
                answer += 10
            elif cnt == 3:
                answer += 100
            else:
                answer += 1000
    return answer


for first, student in enumerate(students.keys()):
    if first == 0:
        room[1][1] = student
        continue
    temp = []
    for y in range(n):
        for x in range(n):
            if room[y][x] == 0:
                like = 0
                empty = 0
                # 사방 확인
                for t in range(4):
                    ny, nx = y + dy[t], x + dx[t]
                    if 0 <= ny < n and 0 <= nx < n:
                        if room[ny][nx] in students[student]:
                            like += 1
                        if room[ny][nx] == 0:
                            empty += 1
                temp.append([like, empty, y, x])
    temp.sort(key=lambda x: (-x[0], -x[1], x[2], x[3]))
    room[temp[0][2]][temp[0][3]] = student


print(calculate(room))
