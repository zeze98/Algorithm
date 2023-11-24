from itertools import combinations_with_replacement


def solution(n, info):
    answer = [-1]
    max_diff = 0
    for combi in combinations_with_replacement(range(11), n):
        apeache = 0
        ryan = 0
        r_info = [0] * 11
        for c in combi:
            r_info[10-c] += 1

        for i in range(11):
            if info[i] == r_info[i] == 0:
                continue
            elif info[i] >= r_info[i]:
                apeache += (10 - i)
            else:
                ryan += (10 - i)

        if ryan > apeache:
            diff = ryan - apeache
            if diff > max_diff:
                max_diff = diff
                answer = r_info

    return answer