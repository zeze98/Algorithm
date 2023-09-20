from collections import deque

def solution(priorities, location):
    answer = 0
    q = deque()
    for idx, pri in enumerate(priorities):
        q.append([idx, pri])
    while q:
        idx, pri = q.popleft()
        if any(pri < qs[1] for qs in q):
            q.append([idx, pri])
        else:
            answer += 1
            if idx == location:
                return answer