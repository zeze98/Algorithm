from collections import deque

def solution(queue1, queue2):
    answer = 0
    queue1 = deque(queue1)
    queue2 = deque(queue2)
    tq1 = sum(queue1)
    tq2 = sum(queue2)
    
    # 두 큐의 길이보다 긴 횟수는 나올 수 없다고 생각함
    limit = len(queue1) + len(queue2)
    
    # 전체 원소의 합이 짝수가 아니면 두 큐의 합을 같게 만들 수 가 없다.
    if (tq1 + tq2) % 2 == 1:
        return -1
    
    while tq1 != tq2:
        if answer >= limit:
            return -1
        
        while queue2 and tq1 < tq2:
            temp = queue2.popleft()
            queue1.append(temp)
            answer += 1
            tq1 += temp
            tq2 -= temp
        while queue1 and tq2 < tq1:
            temp = queue1.popleft()
            queue2.append(temp)
            answer += 1
            tq1 -= temp
            tq2 += temp
                
    return answer