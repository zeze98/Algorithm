def solution(score):
    answer = []
    rank = []
    for i in score:
        rank.append((i[0]+i[1])/2)
    sort_rank = sorted(rank, reverse=True)
    for i in rank:
        answer.append(sort_rank.index(i)+1)

    return answer