s = input().upper()
us = list(set(s))
cnt = []
for i in us:
    cnts = s.count(i)
    cnt.append(cnts)
if cnt.count(max(cnt)) > 1:
    print('?')
else:
    max_index = cnt.index(max(cnt))
    print(us[max_index])
