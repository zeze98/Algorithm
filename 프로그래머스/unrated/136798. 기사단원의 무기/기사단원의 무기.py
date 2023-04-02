def solution(number, limit, power):
    answer = [1]
    for i in range(2, number+1):
        temp = 0
        for j in range(1, int(i**(0.5)) + 1):
            if i % j == 0:
                temp += 1
                if j**2 != i:
                    temp += 1
        if temp > limit:
            answer.append(power)
        else:
            answer.append(temp)
    return sum(answer)