def solution(s):
    answer = []
    for i in s.split():
        try:
            answer.append(int(i))
        except:
            if answer:
                answer.pop()
    return sum(answer)