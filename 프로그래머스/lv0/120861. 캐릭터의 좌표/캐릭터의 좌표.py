def solution(keyinput, board):
    answer = [0, 0]
    max_bord_x = board[0]//2
    max_bord_y = board[1]//2
    for i in keyinput:
        if i == 'left':
            if answer[0] == -max_bord_x:
                pass
            else:
                answer[0] -= 1
        elif i == 'right':
            if answer[0] == max_bord_x:
                pass
            else:
                answer[0] += 1
        elif i == 'up':
            if answer[1] == max_bord_y:
                pass
            else:
                answer[1] += 1
        elif i == 'down':
            if answer[1] == -max_bord_y:
                pass
            else:
                answer[1] -= 1
    return answer