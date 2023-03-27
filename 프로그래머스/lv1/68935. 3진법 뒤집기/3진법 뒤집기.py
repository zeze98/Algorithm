def solution(n):
    answer = ''
    while n >= 1:
        n, r = divmod(n, 3)
        answer += str(r)

    return int(answer,3)