from collections import deque

def solution(people, limit):
    answer = 0
    people = deque(sorted(people))
    while people:
        boat = [people.pop()]
        if people[0] + boat[0] <= limit:
            boat.append(people.popleft())
            answer += 1
        else:
            answer += 1
        if len(people) == 1:
            answer += 1
            break 
        
    return answer