import sys

input = sys.stdin.readline

n, m = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()
answer = []


def dfs(start):
    if len(answer) == m:
        print(' '.join(map(str, answer)))
        return

    for i in range(start, n):
        answer.append(num_list[i])
        dfs(i)
        answer.pop()


dfs(0)