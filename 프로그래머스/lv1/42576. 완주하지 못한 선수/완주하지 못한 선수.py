def solution(participant, completion):

    """
    collection의 counter를 써도 되지만 쓰지 않고 딕셔너리 기능만 써서 풀기    
    """

    # 정답을 딕셔너리 형태로 바꾸기
    answer = {}
    # 모든 참가자를 key 값으로 한뒤 value값의 기본값은 0으로 설정 후 +1 해주기
    # 동명이인 방지를 위해
    for i in participant:
        answer.setdefault(i,0)
        answer[i] += 1

    # 모든 완주자의 value 값을 -1 해주기    
    for j in completion:
        answer[j] -= 1

    # answer 딕셔너리의 key, value 순서를 변경
    answer = {value: key for key, value in answer.items()}

    # 완주하지 못한 한명만 찾으면 되므로 
    return answer.get(1)