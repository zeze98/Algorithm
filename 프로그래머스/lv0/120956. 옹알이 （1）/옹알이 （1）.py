def solution(babbling):
    answer = 0
    baby = ["aya", "ye", "woo", "ma"]
    for i in babbling:
        if 1 < len(i) <= 10:
            cnt = 0
            word = ''
            for j in i:
                word += j
                if word in baby:
                    word = ''
                    cnt += 1
            if len(word) == 0 and cnt > 0:
                answer += 1
    return answer