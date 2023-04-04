def solution(s):
    answer = []
    bin_change = 0
    erase_zero = 0
    while s != '1':
        temp = ''
        for i in s:
            if i == '1':
                temp += '1'
            else:
                erase_zero += 1
        s = bin(len(temp))[2:]
        bin_change +=1
    answer.append(bin_change)
    answer.append(erase_zero)
    return answer