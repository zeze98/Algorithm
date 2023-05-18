from datetime import datetime
import math


def solution(fees, records):
    answer = []
    park = {}
    for i in records:
        t, n, s = i.split()
        if n not in park.keys():
            park[n] = [t]
        else:
            park[n].append(t)
    key = []
    for t in park.keys():
        key.append(t)
    key.sort()
    for i in key:
        temp = 0
        if len(park[i]) % 2 != 0:
            park[i].append('23:59')

        for j in range(0, len(park[i]), 2):
            time_diff = datetime.strptime(
                park[i][j+1], "%H:%M") - datetime.strptime(park[i][j], "%H:%M")
            temp += int(time_diff.seconds / 60)
        if temp <= fees[0]:
            ans = fees[1]
        else:
            ans = fees[1] + (math.ceil((temp - fees[0]) / fees[2]) * fees[3])

        answer.append(ans)
    return answer