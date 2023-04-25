def solution(n, k):
    answer = 0
    temp = ''
    if k == 10:
        temp = str(n)
    else:
        while n > 0:
            n, mod = divmod(n, k)
            temp += str(mod)
        temp = temp[::-1]
    temp = list(filter(None, temp.split('0')))
    for i in temp:
        check = 0
        if int(i) >= 2:
            for j in range(2, int(int(i)**0.5) + 1):
                if int(i) % j == 0:
                    check = 1
                    break
        else:
            continue
        if check == 0:
            answer += 1

    return answer