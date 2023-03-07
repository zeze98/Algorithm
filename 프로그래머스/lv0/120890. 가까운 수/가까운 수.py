def solution(array, n):
    answer = 0
    array.sort()
    check = []
    for i in array:
        check.append(abs(n-i))
    x = check.index(min(check))
    answer = array[x]
    return answer