def solution(n):
    answer = 1
    for i in range(1, n):
        t = i
        for j in range(i+1,n+1):
            t += j
            if t > n:
                break
            elif t == n:
                answer += 1
                break
            
    return answer