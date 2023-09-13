def solution(N, number):
    answer = -1
    temp = []
    for i in range(1, 9):
        t = set()
        t.add(int(str(N) * i))
        for j in range(i - 1):
            for n1 in temp[j]:
                for n2 in temp[-j-1]:
                    t.add(n1 + n2)
                    t.add(n1 - n2)
                    t.add(n1 * n2)
                    if n2 != 0:
                        t.add(n1 // n2)
        if number in t:
            answer = i
            break
        temp.append(t)

    return answer