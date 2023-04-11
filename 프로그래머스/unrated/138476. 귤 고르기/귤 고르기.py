def solution(k, tangerine):
    answer = 0
    size_box=[0]*(max(tangerine)+1)
    for i in tangerine:
        size_box[i] += 1
    size_box.sort(reverse = True)
    i = 0
    while k > 0:
        k -= size_box[i]
        i += 1
        answer += 1  
        
    return answer