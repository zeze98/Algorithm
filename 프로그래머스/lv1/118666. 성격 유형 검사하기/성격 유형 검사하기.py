def solution(survey, choices):
    answer = ''
    temp = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    for i in range(len(survey)):
        if choices[i] <= 3:
            temp[survey[i][0]] += (4-choices[i])
        elif choices[i] == 4:
            continue
        elif choices[i] >= 5:
            temp[survey[i][1]] += (choices[i]-4)
    key_temp = list(temp)
    for i in range(0, len(temp.keys()), 2):
        if temp[key_temp[i]] >= temp[key_temp[i+1]]:
            answer += key_temp[i]
        else:
            answer += key_temp[i+1]
    return answer