def solution(number, k):
    answer = ''
    # 큰 수 담아둘 temp
    temp = []
    
    # numbers의 앞에 오는 수부터 하나씩 비교
    for i in number:
        # i를 int 형으로 변경
        t = int(i)
        
        # 뺄 수 있는 횟수 k 가 0 이상 이어야 하고
        # 비교할 temp에 적어도 하나 이상 원소가 존재해야 하고
        # temp속 마지막 값이 t값 보다 작을때 
        # temp의 마지막 값을 pop 시키고 뺼 수 있는 값인 k 값을 하나씩 줄인다.
        while k > 0 and len(temp) >= 1 and int(temp[-1]) < t:
            temp.pop()
            k -= 1
        # 빼고 난뒤 temp의 마지막에 값을 추가한다. 문자형인 i로 값을 다시 저장
        temp.append(i)
    answer = ''.join(temp)
    return answer[:len(temp) - k]