def solution(my_string):
    answer = 0
    my_string += 'A'
    n = ''
    for i in my_string:
        if i.isnumeric():
            n += i
        else:
            if n.isnumeric():
                answer += int(n)
                n = ''
    return answer