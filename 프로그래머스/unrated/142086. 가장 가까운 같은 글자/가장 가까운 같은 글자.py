def solution(s):
    answer = []
    check_list = []
    for i in range(len(s)):
        if s[i] not in check_list:
            check_list.append(s[i])
            answer.append(-1)
        elif s[i] in check_list:
            close = check_list.index(s[i])
            check_list.append(s[i])
            check_list[close] = 0
            answer.append(len(check_list) - close-1)
    return answer
