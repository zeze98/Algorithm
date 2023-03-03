def solution(numbers):
    answer = 0
    a = max(numbers)
    numbers.pop(numbers.index(max(numbers)))
    b = max(numbers)
    answer = a*b
    return answer