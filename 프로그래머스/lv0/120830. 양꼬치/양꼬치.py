def solution(n, k):
    answer = 0
    a = 0
    if n >= 10:
        a = n//10
    answer = n * 12000 + (k-a)*2000
    return answer