import heapq


def solution(jobs):
    answer, now, cnt = 0, 0, 0
    start = -1
    heap = []

    while cnt < len(jobs):
        for i in jobs:
            if start < i[0] <= now:
                heapq.heappush(heap, [i[1], i[0]])
        if len(heap) > 0:
            current = heapq.heappop(heap)
            start = now
            now += current[0]
            answer += (now - current[1])
            cnt += 1
        else:
            now += 1

    return int(answer / len(jobs))