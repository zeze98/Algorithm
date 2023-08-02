import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_list = sorted(list(map(int, input().split())))
visit = [True] * n
answer = []
# 만든 수열을 담을 공간
temp = []


def dfs(depth, temp):
    # 종료조건
    if depth == m:
        answer.append(temp)
        return

    prev = 0  # 19 19 같은 중복 방지를 위한 이전 수 저장

    for i in range(n):
        if visit[i] and prev != n_list[i]:
            prev = n_list[i]
            visit[i] = False
            dfs(depth + 1, temp + [n_list[i]])
            visit[i] = True


dfs(0, temp)

for i in answer:
    print(*i)
