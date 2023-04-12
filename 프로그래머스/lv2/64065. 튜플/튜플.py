def solution(s):
    answer = []
    s = s[:-2].replace('{', '').replace(',', ' ').split('}')
    for i, v in enumerate(s):
        s[i] = v.split()
    s.sort(key=lambda x:len(x))
    for j in s:
        for k in answer:
            j.remove(k)
        answer.append(j[0])
    answer = [int(i) for i in answer]
    return answer