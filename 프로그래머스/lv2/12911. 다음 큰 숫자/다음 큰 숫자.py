def solution(n):
    answer = 0
    n1 = bin(n)[2:].count('1')
    for i in range(n+1,2000000):
        if bin(i)[2:].count('1') == n1:
            answer = i
            break
    
    return answer