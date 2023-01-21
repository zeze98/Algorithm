n = int(input())
room = []
for i in range(n):
    start, end = map(int, input().split())
    room.append([start, end])

room = sorted(room, key= lambda a : a[0])
room = sorted(room, key= lambda a : a[1])
last = 0
cnt = 0
for i, j in room:
    if i >= last:
        cnt += 1
        last = j
print(cnt)