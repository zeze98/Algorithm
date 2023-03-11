def solution(sides):
    answer = 0
    sides.sort(reverse = True)
    case1 = sides[0]
    for i in range(1, case1):
        if i + sides[1] > case1:
            answer += 1
    case2 = sum(sides) - case1
    answer += case2
    return answer