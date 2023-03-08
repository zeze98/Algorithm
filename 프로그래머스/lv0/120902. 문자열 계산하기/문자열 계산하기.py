def solution(my_string):
    answer = 0
    cal = list(my_string.split())
    pmcheck = 0
    for i in cal:
        if i.isdigit():
            if pmcheck == 0:
                answer += int(i)
            else:
                answer -= int(i)
                pmcheck = 0
        elif i == '-':
            pmcheck = 1

    return answer