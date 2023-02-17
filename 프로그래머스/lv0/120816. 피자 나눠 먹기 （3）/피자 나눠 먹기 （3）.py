def solution(slice, n):
    answer = 0
    a = n // slice
    b = n % slice
    if a>=0 and b>0:
        answer = a + 1
    else:
        answer = a
    return answer