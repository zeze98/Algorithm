def solution(msg):
    answer = []
    word_dic = {}
    for i in range(26):
        word_dic[chr(65 + i)] = i + 1
    x, y = 0, 0
    while True:
        x += 1
        if x == len(msg):
            answer.append(word_dic[msg[y:x]])
            break
        if msg[y:x+1] not in word_dic:
            word_dic[msg[y:x+1]] = len(word_dic) + 1
            answer.append(word_dic[msg[y:x]])
            y = x

    return answer