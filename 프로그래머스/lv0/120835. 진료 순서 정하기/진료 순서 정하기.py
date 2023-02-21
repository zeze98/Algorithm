def solution(emergency):
    answer = [0]*len(emergency)
    for i in range(len(emergency)):
        x = emergency.index(min(emergency))
        answer[x] = len(emergency) - i
        emergency[x] = 101
    return answer