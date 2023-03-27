def solution(s):
    answer = []
    x = s.split(" ")

    for word in x:
        temp = ''
        for idx, i in enumerate(word):
            if idx % 2 == 0:
                temp += i.upper()
            else:
                temp += i.lower()
        answer.append(temp)

    return " ".join(answer)