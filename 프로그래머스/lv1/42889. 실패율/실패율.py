def solution(N, stages):
    answer = []
    fail = {}
    y = len(stages)
    for i in range(1, N+1):
        if y != 0:
            x = stages.count(i)
            fail[i] = x / y
            y = y - x
        else:
            fail[i] = 0
    answer = sorted(fail.keys(), key=lambda x:fail[x], reverse=True)
            
    return answer