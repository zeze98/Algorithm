def solution(cards1, cards2, goal):
    answer = ''
    x = 0
    y = 0
    for i in range(len(goal)):
        if goal[i] == cards1[x]:
            x += 1
            if x == len(cards1):
                x = len(cards1) - 1
            answer = 'Yes'
            continue
        elif goal[i] == cards2[y]:
            y += 1
            if y == len(cards2):
                y = len(cards2) - 1
            answer = 'Yes'
            continue
        elif goal[i] != cards1[x]:
            answer = 'No'
            break
        elif goal[i] != cards2[y]:
            answer = 'No'
            break
    return answer