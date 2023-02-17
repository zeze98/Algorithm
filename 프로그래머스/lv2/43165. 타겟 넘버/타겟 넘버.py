def solution(numbers, target):
    answer = 0
    ln = len(numbers)
    
    def operator(idx=0):
        if idx < ln:
            numbers[idx] *= 1
            operator(idx + 1)
            
            numbers[idx] *= -1
            operator(idx + 1)
        elif sum(numbers) == target:
            nonlocal answer
            answer += 1
    
    operator()
            
    return answer