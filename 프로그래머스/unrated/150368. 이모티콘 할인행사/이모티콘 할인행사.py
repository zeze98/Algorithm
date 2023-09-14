from itertools import product


def solution(users, emoticons):
    answer = [0, 0]
    dc = [10, 20, 30, 40]
    for i in product(dc, repeat=len(emoticons)):
        dc_table = list(i)
        join_user, sell_price = 0, 0
        for r, p in users:
            temp = 0  # 유저별 가격 담기
            for idx, c in enumerate(dc_table):
                if r <= c:
                    temp += (emoticons[idx] * ((100-c)/100))
                else:
                    continue
            if temp >= p:
                join_user += 1
            else:
                sell_price += int(temp)
        if answer[0] < join_user:
            answer[0] = join_user
            answer[1] = sell_price
        elif answer[0] == join_user:
            if answer[1] < sell_price:
                answer[1] = sell_price

    return answer