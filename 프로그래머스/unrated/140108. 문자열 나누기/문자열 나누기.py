def solution(s):
    answer = 0
    while len(s) > 1:
        x = 1
        y = 0
        for i in range(1, len(s)):
            if s[i] == s[0]:
                x += 1
            else:
                y += 1
            if x == y:
                s = s[i+1:]
                answer += 1
                break
        if x != y:
            answer += 1
            break
    if len(s) == 1:
        answer += 1
    return answer