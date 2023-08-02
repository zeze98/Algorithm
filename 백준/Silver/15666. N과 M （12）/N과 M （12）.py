import sys

input = sys.stdin.readline

n, m = map(int, input().split())
n_list = sorted(list(set(map(int, input().split()))))
# 만든 수열을 담을 공간
temp = []


def dfs(depth):
    # 종료조건
    if depth == m:
        print(" ".join(map(str, temp)))
        return

    for i in range(len(n_list)):
        if depth == 0 or temp[-1] <= n_list[i]:
            temp.append(n_list[i])
            dfs(depth + 1)
            temp.pop()


dfs(0)
