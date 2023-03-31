def check_rank(match_num):
    if match_num == 6:
        return 1
    elif match_num == 5:
        return 2
    elif match_num == 4:
        return 3
    elif match_num == 3:
        return 4
    elif match_num == 2:
        return 5
    else:
        return 6


def solution(lottos, win_nums):
    answer = []
    match_num = 0
    for i in lottos:
        if i == 0:
            match_num += 1
        elif i in win_nums:
            match_num += 1
    answer.append(check_rank(match_num))
    match_num = 0
    for i in lottos:
        if i in win_nums:
            match_num += 1
    answer.append(check_rank(match_num))
    
    return answer
