def solution(s):
    new_s = [0]
    for i in s:
        if i == new_s[-1]:
            new_s.pop()
        elif i != new_s[-1]:
            new_s.append(i)
    
    if len(new_s) == 1:
        return 1
    else:
        return 0