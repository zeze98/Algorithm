from collections import deque


def solution(prices):
    answer = []
    q = deque(prices)
    while q:
        time = 0
        now = q.popleft()
        for future in q:
            time += 1
            if now > future:
                break
        answer.append(time)
    return answer