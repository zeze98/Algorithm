def solution(elements):
    answer = set([sum(elements)])
    for i in range(1, len(elements)):
        total = sum(elements[:i])
        start, end = 0, i
        for _ in range(len(elements)):
            total += elements[end] - elements[start]
            start, end = start + 1, (end+1) % len(elements)
            answer.add(total)
    return len(answer)