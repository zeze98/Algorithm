def solution(s):

    word = s.split(' ')
    temp = []
    for i in word:
        i = i.capitalize()
        temp.append(i)
        
    return " ".join(temp)