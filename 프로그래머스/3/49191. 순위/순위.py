def solution(n, results):
    answer = 0
    record = [[0] * n for _ in range(n)]
    for winner, loser in results:
        record[winner - 1][loser - 1] = 1
        record[loser - 1][winner - 1] = -1

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if i == j or record[i][j] in [1, -1]:
                    continue
                if record[i][k] == record[k][j] == 1:
                    record[i][j] = 1
                    record[j][i] = record[k][i] = record[j][k] = -1

    for row in record:
        if row.count(0) == 1:
            answer += 1
    return answer