def solution(n, words):
    answer = [0,0]
    new_words = []
    error_check = 0
    for i in words:
        if len(new_words) > 0:
            if i in new_words:
                new_words.append(i)
                error_check += 1
                break
            elif i not in new_words:
                new_words.append(i)
                if i[0] != new_words[-2][-1]:
                    error_check += 1
                    break
        else:
            new_words.append(i)
    if error_check == 0:
        return answer
    else:
        turn, people = divmod(len(new_words), n)
        turn += 1
        if people == 0:
            people = n
            turn -= 1
        answer[0] = people
        answer[1] = turn
        return answer