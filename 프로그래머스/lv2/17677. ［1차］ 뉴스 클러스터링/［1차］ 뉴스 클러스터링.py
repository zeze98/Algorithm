def solution(str1, str2):
    answer = 0
    a = []
    b = []
    for i in range(len(str1)-1):
        temp = str1[i]+str1[i+1]
        if temp.isalpha():
            a.append(temp.lower())
    for i in range(len(str2)-1):
        temp = str2[i]+str2[i+1]
        if temp.isalpha():
            b.append(temp.lower())
    A = []
    for j in set(a+b):
        x = a.count(j)
        y = b.count(j)
        z = min(x, y)
        A.append(z)
    B = []
    for j in set(a+b):
        x = a.count(j)
        y = b.count(j)
        z = max(x, y)
        B.append(z)
    if sum(A) != 0 and len(B) != 0:
        answer = int((sum(A)/sum(B)) * 65536)
    elif sum(A) == 0 and len(B) != 0:
        answer = 0
    else:
        answer = 65536
    return answer