def solution(s):
    answer = 0
    temp = list(s)
    
    for _ in range(len(s)):
 
        temp_s = []
        for i in range(len(temp)):
            if len(temp_s) > 0:
                if temp_s[-1] == '[' and temp[i] == ']':
                    temp_s.pop()
                elif temp_s[-1] == '(' and temp[i] == ')':
                    temp_s.pop()
                elif temp_s[-1] == '{' and temp[i] == '}':
                    temp_s.pop()
                else:
                    temp_s.append(temp[i])
            else:
                temp_s.append(temp[i])
        if len(temp_s) == 0:
            answer += 1
        temp.append(temp.pop(0))
 
    return answer