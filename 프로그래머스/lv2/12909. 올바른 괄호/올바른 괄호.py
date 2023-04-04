def solution(s):
    answer = True
    temp = []
    for i in s:
        if i == ')' and len(temp) == 0:
            answer = False
        elif i == '(':
            temp.append(i)
        elif i ==')':
            if temp[-1] == '(':
                temp.pop()
    if len(temp) > 0:
        answer = False
    return answer