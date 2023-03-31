def solution(dartResult):
    answer = 0
    temp = []
    num_temp = ''
    for i in range(len(dartResult)):
        if dartResult[i].isdigit():
            num_temp += dartResult[i]
        elif dartResult[i] == 'S':
            temp.append(int(num_temp)**1)
            num_temp = ''
        elif dartResult[i] == 'D':
            temp.append(int(num_temp)**2)
            num_temp = ''
        elif dartResult[i] == 'T':
            temp.append(int(num_temp)**3)
            num_temp = ''
        elif dartResult[i] == '*':
            temp[-1] = temp[-1]*2
            if len(temp)>=2:
                temp[-2] = temp[-2]*2
        elif dartResult[i] == '#':
            temp[-1] = temp[-1]*(-1)
    answer = sum(temp)
    return answer