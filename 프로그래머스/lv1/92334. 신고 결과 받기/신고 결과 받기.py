def solution(id_list, report, k):
    answer = []
    id_dic = {i: [0] for i in id_list}
    repot_list = []
    set_report = list(set(report))
    for i in set_report:
        user, repot = i.split()
        id_dic[user].append(repot)
        id_dic[repot][0] += 1

    for i in id_dic.keys():
        for j in id_dic[i]:
            if type(j) == int and j >= k:
                repot_list.append(i)

    for i in id_dic.keys():
        temp = 0
        id_dic[i].append(temp)
        for j in id_dic[i]:
            if j in repot_list:
                id_dic[i][-1] += 1

    for i in id_dic.keys():
        answer.append(id_dic[i][-1])
    return answer
