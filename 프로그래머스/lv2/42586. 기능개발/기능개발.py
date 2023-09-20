def solution(progresses, speeds):
    answer = []
    temp = []
    file = 1
    for i in range(len(speeds)):
        fin_date = (100 - progresses[i]) / speeds[i]
        if fin_date != int(fin_date):
            fin_date = int(fin_date) + 1
        temp.append(int(fin_date))
    
    for n in range(1, len(temp)):
        if temp[n] <= temp[n-1]:
            temp[n] = temp[n-1]
            file +=1
        else:
            answer.append(file)
            file = 1
    answer.append(file)
    return answer