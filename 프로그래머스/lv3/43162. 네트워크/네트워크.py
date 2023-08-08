from collections import deque


def solution(n, computers):
    answer = 0
    visit = [False] * n

    def find_network(start):
        visit[start] = True
        for near in range(n):
            if visit[near] == False and computers[start][near] == 1:
                find_network(near)

    for i in range(n):
        if visit[i] == False:
            find_network(i)
            answer += 1

    return answer