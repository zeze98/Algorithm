def solution(d, budget):
    answer = 0
    d.sort()
    for i in d:
        if i <= budget:
            answer += 1
            budget -= i
        elif i > budget:
            break
    return answer