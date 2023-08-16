def solution(name):
    answer = 0
    wide = len(name) - 1

    for i, char in enumerate(name):
        answer += min(ord(char) - ord('A'), ord('Z') - ord(char) + 1)

        next = i + 1
        while next < len(name) and name[next] == 'A':
            next += 1

        wide = min([wide, 2 * i + len(name) - next,
                   i + 2 * (len(name) - next)])

    answer += wide

    return answer