def solution(before, after):
    answer = 1
    before = list(before)
    after = list(after)
    for i in before:
        if i not in after:
            answer = 0
            break
        elif i in after:
            after.remove(i)
    return answer