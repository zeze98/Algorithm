def solution(files):
    answer = []
    sep_fi = []
    for file in files:
        head = ''
        number = ''
        tail = ''
        n_check = 0
        tail_check = 0
        for idx in range(len(file)):
            if file[idx].isdecimal() == True and tail_check == 0:
                number += file[idx]
                n_check = 1
            elif file[idx].isdecimal() == False and n_check == 0:
                head += file[idx]
            else:
                tail += file[idx]
                tail_check = 1
        temp = [head, number, tail]
        sep_fi.append(temp)
    sep_fi = sorted(sep_fi, key = lambda x:(x[0].lower(), int(x[1])))
    for s_f in sep_fi:
        answer.append(''.join(s_f))
    return answer