def solution(today, terms, privacies):
    answer = []
    year, month, day = int(today[0:4]), int(today[5:7]), int(today[8:])
    dic_term = dict()
    for t in terms:
        key = t[0]
        dic_term[key] = int(t[2:])

    for i in range(len(privacies)):
        date, case = privacies[i].split()
        pri_year, pri_month, pri_day = int(privacies[i][0:4]), int(privacies[i][5:7]), int(privacies[i][8:10])

        pri_month += dic_term[case]

        while pri_month > 12:
            pri_month -= 12
            pri_year += 1
        if pri_year > year:
            continue
        elif pri_year == year:
            if pri_month > month:
                continue
            elif pri_month == month:
                if pri_day > day:
                    continue
        answer.append(i+1)
    return answer