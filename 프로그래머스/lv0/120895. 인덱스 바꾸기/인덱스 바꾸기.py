def solution(my_string, num1, num2):
    answer = ''
    x = my_string[num1]
    y = my_string[num2]
    for i in range(len(my_string)):
        if i == num1:
            answer += y
        elif i == num2:
            answer += x
        else:
            answer += my_string[i]

    return answer