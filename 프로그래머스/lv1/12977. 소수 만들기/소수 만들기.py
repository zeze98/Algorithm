def is_prime(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

def solution(nums):
    answer = 0

    for i in range(len(nums)-2):
        for j in range(i+1, len(nums)-1):
            for k in range(j+1, len(nums)):
                t = nums[i] + nums[j] + nums[k]
                if is_prime(t):
                    answer += 1

    return answer