def solution(dots):
    x = [dot[0]for dot in dots]
    y = [dot[1]for dot in dots]
    w = max(x) - min(x)
    d = max(y) - min(y)
    answer = w *d
    return answer