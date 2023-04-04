pad = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9],
       ['*',0,'#']]

def check_index(i):
    for y in range(4):
        for x in range(3):
            if pad[y][x] == i:
                return [y,x]


def check_hands(x, left_hand, right_hand, hand):
    button = check_index(x)
    l, r = 0,0
    for i in range(2):
        l += abs(button[i] - left_hand[i])
    for i in range(2):
        r += abs(button[i] - right_hand[i])
    if l < r:
        return 'L'
    elif r < l:
        return 'R'
    else:
        if hand == 'right':
            return 'R'
        else:
            return 'L'

def solution(numbers, hand):
    answer = ''
    left = [1, 4, 7]
    right = [3, 6, 9]
    check = [2, 5, 8, 0]
    left_temp = [[3,0]]
    right_temp = [[3,2]]
    for i in numbers:
        if i in left:
            answer += 'L'
            left_temp.append(check_index(i))
        elif i in right:
            answer += 'R'
            right_temp.append(check_index(i))
        else:
            answer += check_hands(i, left_temp[-1], right_temp[-1], hand)
            if check_hands(i, left_temp[-1], right_temp[-1], hand) == 'L':
                left_temp.append(check_index(i))
            else:
                right_temp.append(check_index(i))
    return answer