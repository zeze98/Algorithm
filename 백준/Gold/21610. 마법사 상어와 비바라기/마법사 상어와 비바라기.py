import sys

input = sys.stdin.readline

n, m = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(n)]
clouds = [[n-1, 0], [n-1, 1], [n-2, 0], [n-2, 1]]
direction = [[0, -1], [-1, -1], [-1, 0],
             [-1, 1], [0, 1], [1, 1], [1, 0], [1, -1]]
water_copy = [[1, 1], [1, -1], [-1, -1], [-1, 1]]
answer = 0
for i in range(m):
    d, s = map(int, input().split())
    new_clouds = []
    temp = []
    visit = [[True] * n for _ in range(n)]
    # 구름 이동후 비뿌리기
    for cn in range(len(clouds)):
        cy, cx = clouds[cn][0], clouds[cn][1]
        new_cy, new_cx = cy + (direction[d-1][0]*s), cx + (direction[d-1][1]*s)
        new_cy %= n
        new_cx %= n
        table[new_cy][new_cx] += 1
        temp.append([new_cy, new_cx])
        visit[new_cy][new_cx] = False

    # 물복사
    for ncn in range(len(temp)):
        ncy, ncx = temp[ncn][0], temp[ncn][1]
        for j in range(4):
            dncy, dncx = ncy + water_copy[j][0], ncx + water_copy[j][1]
            if 0 <= dncy < n and 0 <= dncx < n and table[dncy][dncx] > 0:
                table[ncy][ncx] += 1

    # 구름 생성
    for y in range(n):
        for x in range(n):
            if visit[y][x] == True and table[y][x] >= 2:
                new_clouds.append([y, x])
                table[y][x] -= 2
    clouds = new_clouds

for check in table:
    answer += sum(check)

print(answer)