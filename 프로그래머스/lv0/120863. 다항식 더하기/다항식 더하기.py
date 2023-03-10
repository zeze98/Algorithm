def solution(polynomial):
    answer = ''
    pol = polynomial.split(' + ')
    x = []
    num = []
    for i in pol:
        if i.isnumeric():
            num.append(int(i))
        else:
            if i.split('x')[0].isnumeric():
                x.append(int(i.split('x')[0]))
            elif i.split('x')[0] == '':
                x.append(1)
    if len(x) != 0:
        if sum(num) != 0:
            if sum(x) == 1:
                answer = 'x + ' + str(sum(num))
            else:
                answer = str(sum(x))+'x' + ' + '+str(sum(num))
        else:
            if sum(x) == 1:
                answer = 'x'
            else:
                answer = str(sum(x)) + 'x'
    else:
        if sum(num) != 0:
            answer = str(sum(num))
        else:
            answer = 0
    return answer