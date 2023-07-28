import heapq


def solution(operations):
    answer = []
    heap = []
    for i in operations:
        order, number = i.split()
        if order == 'I':
            heapq.heappush(heap, int(number))
        elif order == 'D':
            if not heap:
                continue
            if number == '-1':
                heapq.heappop(heap)
            elif number == '1':
                heap.sort()
                heap.pop()

    if len(heap) >= 2:
        answer.append(max(heap))
        answer.append(min(heap))
    else:
        answer = [0, 0]
    return answer