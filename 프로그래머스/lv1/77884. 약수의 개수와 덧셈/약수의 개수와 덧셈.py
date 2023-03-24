def solution(left, right):
    answer = 0
    check = []
    for i in range(left, right+1):
        for j in range(1,i+1):
            if i % j == 0:
                check.append(j)
        if len(check)%2 == 0:
            answer += i
            check = []
        else:
            answer -= i
            check = []
    return answer