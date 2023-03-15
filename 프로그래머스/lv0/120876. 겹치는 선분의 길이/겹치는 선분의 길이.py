def solution(lines):
    answer = 0
    table = [set([]) for _ in range(200)]
    for index, line in enumerate(lines):
        a, b = line
        for i in range(a,b):
            table[i].add(index)
    for line in table:
        if len(line) > 1:
            answer += 1
    return answer