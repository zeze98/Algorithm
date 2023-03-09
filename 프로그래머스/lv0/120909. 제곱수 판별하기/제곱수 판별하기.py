def solution(n):
    answer = 2
    if n **(1/2) % 1 == 0:
        answer = 1
    return answer