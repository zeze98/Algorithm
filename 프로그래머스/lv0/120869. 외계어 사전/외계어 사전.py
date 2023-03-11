def solution(spell, dic):
    spell = {x : 0 for x in spell}
    answer = 2
    for i in dic:
        if len(i) == len(spell):
            for j in i:
                if j in spell:
                    spell[j] += 1
                else:
                    break
            if len(set(spell.values())) == 1 and sum(set(spell.values())) == 1:
                answer = 1
            spell = {x : 0 for x in spell}

    return answer