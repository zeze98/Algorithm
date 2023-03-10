def solution(my_str, n):
    answer = []
    x = ''
    for i in my_str:
        x += i
        if len(x) == n:
            answer.append(x)
            x = ''
    if len(x)>=1:
        answer.append(x)
    return answer
