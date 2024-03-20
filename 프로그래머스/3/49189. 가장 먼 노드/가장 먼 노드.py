from collections import deque


def solution(n, edge):
    answer = [[1]]
    tree = [[] for _ in range(n+1)]
    q = deque([[1]])
    visit = [[True] for _ in range(n+1)]

    for a, b in edge:
        tree[a].append(b)
        tree[b].append(a)

    while q:
        start = q.popleft()
        temp = []
        for i in start:
            visit[i] = False
        for j in start:
            for node in tree[j]:
                if visit[node]:
                    temp.append(node)
        temp = list(set(temp))
        if len(temp) == 0:
            break
        q.append(temp)
        answer.append(temp)

    return len(answer[-1])