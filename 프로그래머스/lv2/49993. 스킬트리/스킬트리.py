def solution(skill, skill_trees):
    answer = 0
    t_d = {}
    for i in range(len(skill)-1, 0, -1):
        t_d[skill[i]] = skill[i - 1]
    t_d[skill[0]] = ''

    for tree in skill_trees:
        temp = ['']
        flag = 0
        for s in tree:
            if s in t_d.keys() and t_d[s] not in temp:

                flag = 1
                break
            elif s in t_d.keys():
                temp.append(s)
        if flag == 0:
            answer += 1
    return answer