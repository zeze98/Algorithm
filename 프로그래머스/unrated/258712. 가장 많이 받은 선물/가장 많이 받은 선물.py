def solution(friends, gifts):
    answer = 0
    table = {}

    # 선물 테이블 만들기
    for friend in friends:
        table[friend] = {'선물지수': 0}
        for name in friends:
            if name != friend:
                table[friend][name] = 0

    # 선물지수
    for i in gifts:
        give, take = i.split()
        table[give][take] += 1
        table[give]['선물지수'] += 1
        table[take]['선물지수'] -= 1

    # 선물 주고 받기
    for friend in friends:
        final = 0
        friend_gift_score = table[friend]['선물지수']
        for other_f in table[friend]:
            if other_f != '선물지수':
                if table[friend][other_f] == table[other_f][friend]:
                    if table[friend]['선물지수'] > table[other_f]['선물지수']:
                        final += 1
                elif table[friend][other_f] > table[other_f][friend]:
                    final += 1
        answer = max(final, answer)
    return answer