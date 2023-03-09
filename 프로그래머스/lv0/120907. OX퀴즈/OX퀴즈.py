def solution(quiz):
    answer = []
    for i in quiz:
        q, a = i.split('=')
        if eval(q) == int(a):
            answer.append('O')
        else:
            answer.append('X')

    return answer
