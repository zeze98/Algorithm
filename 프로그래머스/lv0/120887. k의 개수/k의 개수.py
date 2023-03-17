def solution(i, j, k):
    answer = 0

    for t in range(i, j+1):
        tt = list(str(t))
        if str(k) in tt:
            for q in range(len(tt)):
                if tt[q]==str(k):
                    answer += 1
    return answer
