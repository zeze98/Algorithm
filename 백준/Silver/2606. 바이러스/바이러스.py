def dfs(start):
    global cnt
    visited[start] = 1
    for i in com[start]:
        if visited[i] == 0:
            dfs(i)
            cnt += 1

cn = int(input())
nn = int(input())
com = [[]*cn for _ in range(cn+1)]
for _ in range(nn):
    x, y = map(int, input().split())
    com[x].append(y)
    com[y].append(x)

cnt = 0
visited = [0] * (cn+1)

dfs(1)
print(cnt)