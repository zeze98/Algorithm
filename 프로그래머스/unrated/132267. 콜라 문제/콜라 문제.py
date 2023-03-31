def solution(a, b, n):
    answer = 0
    cola = n
    while cola >= a:
        x, y = divmod(n, a)
        cola = x*b +y
        answer += (x*b)
        n = cola
    
    return answer