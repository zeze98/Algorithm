def solution(n, arr1, arr2):
    answer = []
    bin_arr1 = []
    bin_arr2 = []
    temp = ''
    for i in arr1:
        x = bin(i)
        x = x[2:]
        while len(x) != n:
            x = '0'+ x
        bin_arr1.append(x)
    for j in arr2:
        y = bin(j)
        y = y[2:]
        while len(y) != n:
            y = '0'+ y
        bin_arr2.append(y)
    
    for q in range(n):
        for p in range(n):
            if int(bin_arr1[q][p]) + int(bin_arr2[q][p]) > 0:
                temp += '#'
            else:
                temp += ' '
        answer.append(temp)
        temp = ''
    
    return answer