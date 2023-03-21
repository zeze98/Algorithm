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

    for i in num_list:
        if i not in answer:
            answer.append(i)
            dfs(i+1)
            answer.pop()


dfs(num_list[0])