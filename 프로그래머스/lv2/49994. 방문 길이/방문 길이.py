def solution(dirs):
    answer = 0
    start = [5, 5]
    path = set()
    or_dic = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}

    for t in dirs:
        dx, dy = or_dic[t]
        nx = start[0] + dx
        ny = start[1] + dy
        if 0 <= nx <= 10 and 0 <= ny <= 10:
            path.add(((nx, ny), (start[0], start[1])))
            path.add(((start[0], start[1]), (nx, ny)))
            start = [nx, ny]
    answer = len(path) // 2
    return answer
