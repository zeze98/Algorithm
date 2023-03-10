def solution(numbers):
    numbers.sort(reverse=True)
    answer = max(numbers[0]*numbers[1],numbers[-1]*numbers[-2])
    return answer