def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    start = 3600*h1 + 60*m1 + s1
    end = 3600*h2 + 60*m2 + s2
    ring = {}

    for t in range(24*3600):
        ring[t] = {'cur': 0, 'after': 0}

    ps, pm, ph = 0, 0, 0

    for t in range(1, 24*3600):
        aftercnt, curcnt = 0, 0
        cs, cm, ch = 6*t % 360, (t/10) % 360, (t/120) % 360

        if ps < pm and cs > cm:
            aftercnt += 1
        elif ps < pm and cs == 0:
            aftercnt += 1
        elif cs == cm:
            curcnt += 1

        if ps < ph and cs > ch:
            aftercnt += 1
        elif ps < ph and cs == 0:
            aftercnt += 1
        elif cs == ch:
            curcnt += 1

        if t != 3600 * 12:
            if curcnt != 0:
                ring[t]['cur'] += curcnt
            if aftercnt != 0:
                ring[t-1]['after'] += aftercnt

        ps, pm, ph = cs, cm, ch
    ring[0] = {'cur': 1, 'after': 0}
    ring[3600*12] = {'cur': 1, 'after': 0}

    for time in range(start, end):
        if time in ring:
            answer += ring[time]["after"]
            answer += ring[time]["cur"]
    answer += ring[end]['cur']
    return answer