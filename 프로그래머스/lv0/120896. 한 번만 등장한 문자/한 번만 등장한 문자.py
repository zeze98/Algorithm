def solution(s):
    word_dic = {}
    for i in s:
        if i not in word_dic.keys():
            word_dic[i] = 1
        else:
            word_dic[i] += 1

    answer = [k for k, v in word_dic.items() if v == 1]
    answer.sort()
    answer = ''.join(answer)
    return answer