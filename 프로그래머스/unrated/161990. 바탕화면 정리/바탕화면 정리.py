def solution(wallpaper):
    answer = []
    desktop = []
    s = []
    e = []
    for y in range(len(wallpaper)):
        temp = []
        for x in range(len(wallpaper[y])):
            if wallpaper[y][x] == '#':
                temp.append(x)
        desktop.append(temp)
        if len(temp) > 0:
            s.append(y)
        e += temp

    answer.append(min(s))
    answer.append(min(e))
    answer.append(max(s)+1)
    answer.append(max(e)+1)
    return answer