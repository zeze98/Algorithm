def solution(triangle):
    dp = triangle
    if len(triangle) == 1:
        return dp[0][0]
    if len(triangle) == 2:
        dp[1][0] += dp[0][0]
        dp[1][1] += dp[0][0]
        return max(dp[1][0], dp[1][1])
    else:
        dp[1][0] += dp[0][0]
        dp[1][1] += dp[0][0]
        for i in range(2, len(triangle)):  # 0층 과 1층은 값을 미리 저장함 2층 이상부터의 층수 계산
            for j in range(i+1):  # i층 에서 의 원소들
                if j == 0:  # 각 층의 0번 째 번호는 정해져 있다.
                    dp[i][0] += dp[i-1][0]
                elif j == i: # 마찬 가지로 각 층의 마지막 번호는 정해져 있다
                    dp[i][i] += dp[i-1][i-1]
                else: # 중간 부분에서는 위층의 둘중하나에서 더 큰 값 선택해야함
                    dp[i][j] += max(dp[i-1][j-1], dp[i-1][j])
    return max(dp[-1])