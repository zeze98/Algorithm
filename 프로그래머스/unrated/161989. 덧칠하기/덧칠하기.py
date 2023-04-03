def solution(n, m, section):
    answer = 0
    temp = 0
    for i in section:
        if i > temp:
            answer += 1
            temp = i + m -1
    
    return answer