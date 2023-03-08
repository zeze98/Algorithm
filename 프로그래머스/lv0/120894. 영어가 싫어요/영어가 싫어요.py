def solution(numbers):
    answer = ''
    ndic = {'zer': '0', 'on': '1', 'tw': '2', 'thre': '3', 'fou': '4', 'fiv': '5', 'si': '6', 'seve': '7',
            'eigh': '8', 'nin': '9'}
    n = ''
    for i in numbers:
        if n in ndic.keys():
            answer += ndic[n]
            n = ''
        else:
            n += i
    return int(answer)