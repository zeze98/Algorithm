def solution(n):
    answer = 0
    for i in range(max(6,n), (6*n) + 1):
        if i % 6 == 0 and i % n == 0:
            answer = i//6
            break
    return answer