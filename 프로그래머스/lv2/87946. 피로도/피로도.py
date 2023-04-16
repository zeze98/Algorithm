from itertools import permutations


def solution(k, dungeons):
    answer = -1
    all_chance = []
    for i in permutations(dungeons, len(dungeons)):
        all_chance.append(list(i))
    pos = []
    j = 0
    while j < len(all_chance):
        sta = k
        count = 0
        for q in all_chance[j]:
            if sta >= q[0]:
                sta = sta - q[1]
                count += 1
            elif sta < q[0]:
                break
        pos.append(count)
        j += 1
    answer = max(pos)
    return answer