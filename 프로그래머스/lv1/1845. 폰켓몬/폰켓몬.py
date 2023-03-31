def solution(nums):
    answer = 0
    pick = len(nums)//2
    take = set(nums)
    if len(take) >= pick:
        answer = pick
    else:
        answer = len(take)
    
    return answer