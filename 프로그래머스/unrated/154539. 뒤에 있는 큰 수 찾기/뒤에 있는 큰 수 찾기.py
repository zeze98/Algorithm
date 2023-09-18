def solution(numbers):
    answer = [-1] * len(numbers)
    temp = []
    
    for i in range(len(numbers)):
        while temp and numbers[temp[-1]] < numbers[i]:
            answer[temp.pop()] = numbers[i]
        temp.append(i)
    
    return answer