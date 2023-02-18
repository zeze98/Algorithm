def solution(array):
    check = [0 for _ in range(1001)]
    for i in array:
        check[i] += 1
    cnt = check.count(max(check))
    if cnt > 1:
        answer = -1
    else:
        answer = check.index(max(check))
    return answer