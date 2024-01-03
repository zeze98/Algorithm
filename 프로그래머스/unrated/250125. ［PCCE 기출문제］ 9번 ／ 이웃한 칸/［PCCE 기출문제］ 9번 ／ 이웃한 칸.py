def solution(board, h, w):
    answer = 0
    cor = board[h][w]
    n = len(board)

    if 0 <= h - 1:
        if cor == board[h-1][w]:
            answer += 1
    if n > h + 1:
        if cor == board[h+1][w]:
            answer += 1
    if 0 <= w - 1:
        if cor == board[h][w-1]:
            answer += 1
    if n > w+1:
        if cor == board[h][w+1]:
            answer += 1

    return answer