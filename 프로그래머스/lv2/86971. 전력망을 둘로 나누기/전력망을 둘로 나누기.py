from collections import deque


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n+1)]

    for v1, v2 in wires:
        graph[v1].append(v2)
        graph[v2].append(v1)

    def bfs(start):
        visited = [False] * (n+1)
        q = deque([start])
        visited[start] = True
        cnt = 1
        while q:
            s = q.popleft()
            for i in graph[s]:
                if not visited[i]:
                    q.append(i)
                    visited[i] = True
                    cnt += 1
        return cnt

    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        answer = min(abs(bfs(v1) - bfs(v2)), answer)
        graph[v1].append(v2)
        graph[v2].append(v1)

    return answer