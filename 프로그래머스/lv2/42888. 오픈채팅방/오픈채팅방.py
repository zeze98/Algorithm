def solution(record):
    answer = []
    dic = {}
    for i in record:
        stat = i.split()[0]
        uid = i.split()[1]
        if stat != 'Leave':
            nick = i.split()[2]
            dic[uid] = nick
    for i in record:
        stat = i.split()[0]
        uid = i.split()[1]
        if stat == 'Enter':
            answer.append(dic[uid] + '님이 들어왔습니다.')
        elif stat == 'Leave':
            answer.append(dic[uid] + '님이 나갔습니다.')

    return answer