def solution(keymap, targets):
    answer = []
    key_dic = {}
    for i in keymap:
        for j, letter in enumerate(i):
            if letter not in key_dic.keys():
                key_dic[letter] = j
            else:
                key_dic[letter] = min(j, key_dic[letter])
    for x in targets:
        temp = 0
        for y in x:
            if y not in key_dic.keys():
                temp = -1
                break
            else:
                temp += key_dic[y] + 1
        answer.append(temp)

    return answer