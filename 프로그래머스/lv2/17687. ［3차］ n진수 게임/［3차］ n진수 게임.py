def convert_notation(n, base):
    T = "0123456789ABCDEF"
    q, r = divmod(n, base)

    return convert_notation(q, base) + T[r] if q else T[r]

def solution(n, t, m, p):
    answer = ''
    all_num = ''
    i = 0
    while True:
        if len(all_num) >= t*m:
            break
        x = convert_notation(i,n)
        all_num += x
        i += 1
    cnt = 1
    while len(answer) < t:
        answer += all_num[(p-1) + (m*(cnt-1))]
        cnt += 1

    return answer