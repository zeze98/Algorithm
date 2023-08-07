import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())
city = [list(map(int, input().split())) for _ in range(n)]
# 0 빈칸, 1 집, 2 치킨
# 집의 갯수는 최대 2N 안넘음
# 치킨 집의 갯수는 M 보다 크거나 같다, 13보다 작거나 같다
# m <= 치킨집 <= 13
chicken = []
house = []
answer = 1000000
for i in range(len(city)):
    for j in range(len(city[i])):
        if city[i][j] == 2:
            chicken.append([i, j])
        if city[i][j] == 1:
            house.append([i, j])

for chick in combinations(chicken, m):
    temp = 0
    for hou in house:
        chicken_road = 100
        for i in range(m):
            chicken_road = min(chicken_road, abs(
                hou[0] - chick[i][0]) + abs(hou[1] - chick[i][1]))
        temp += chicken_road
    answer = min(answer, temp)
print(answer)
