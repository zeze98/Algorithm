def solution(m, n, puddles):
    # m = x, n = y
    # 집 = 가장 왼쪽위, 학교 = 가장 오른 쪽 아래
    dp = [[1] * m for _ in range(n)]
    for x, y in puddles:
        if x == 1:
            for i in range(y-1, n):
                dp[i][x-1] = 0
        elif y == 1:
            for j in range(x-1, m):
                dp[y-1][j] = 0
        dp[y-1][x-1] = 0
    dp[0][0] = 0
    # for i in dp:
    #     print(i)
    # print('================================')
    for y in range(1, n):
        for x in range(1, m):
            if dp[y][x] != 0:
                dp[y][x] = dp[y-1][x] + dp[y][x-1]
    # for i in dp:
    #     print(i)

    answer = dp[n-1][m-1] % 1000000007
    return answer