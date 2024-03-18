import heapq


def solution(n, works):
    if sum(works) - n <= 0:
        return 0

    result = [-work for work in works]
    heapq.heapify(result)
    for _ in range(n):
        work = heapq.heappop(result)
        work += 1
        heapq.heappush(result, work)
    answer = sum([work ** 2 for work in result])
    return answer