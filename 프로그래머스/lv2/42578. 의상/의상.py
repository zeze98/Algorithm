def solution(clothes):
    answer = 1
    closet = {}
    for c_name, c_type in clothes:
        closet[c_type] = closet.get(c_type,[]) + [c_name]

    for k in closet.keys():
        answer *= (len(closet[k]) + 1)
    return answer - 1