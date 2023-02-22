def solution(num_list, n):
    answer = [[0 for _ in range(n)]for _ in range(len(num_list) // n)]
    x = 0
    y = 0
    for i in num_list:
        answer[x][y] = i
        y += 1
        if y == n:
            y = 0
            x += 1
        if x == len(num_list) // n:
            x = 0   
    return answer