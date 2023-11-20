def solution(alp, cop, problems):
    max_alp = 0
    max_cop = 0
    time = 0
    # 문제를 전부 풀기위한 알고력과 코딩력 찾기
    for a,b,c,d,e in problems:
        max_alp = max(max_alp,a)
        max_cop = max(max_cop,b)
        #문제를 적어도 한번씩이라도 푸는데 걸리는 시간
        time += e
    
   # 
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    INF = float('inf')
    dp = [[INF]*(max_cop + 1) for _ in range(max_alp + 1)]
    dp[alp][cop] = 0
    for i in range(alp, max_alp + 1):
        for j in range(cop, max_cop + 1):
            # 목표로 하는 능력치 보다 낮은 능력치는 1씩 더해서 찾음
            if i + 1 <= max_alp:
                dp[i + 1][j] = min (dp[i + 1][j],dp[i][j] + 1)
            if j + 1 <= max_cop:
                dp[i][j + 1] = min (dp[i][j + 1],dp[i][j] + 1)
            
            # 풀수 있는 문제의 경우 dp판에서 능력치 업데이트
            for alp_req,cop_req,alp_rwd,cop_rwd,cost in problems:
                if i >= alp_req and j >= cop_req:
                    next_alp,next_cop = min(max_alp,i + alp_rwd), min(max_cop,j + cop_rwd)
                    dp[next_alp][next_cop] = min(dp[next_alp][next_cop],dp[i][j] + cost)
    

    return dp[-1][-1]
                    