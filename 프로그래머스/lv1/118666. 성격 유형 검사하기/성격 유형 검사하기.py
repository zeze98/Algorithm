def solution(survey, choices):
    answer = ''
    
    # 각 성격 들의 점수를 담을 수 있는 딕셔너리
    personality = {'R': 0, 'T': 0, 'C': 0, 'F': 0, 'J': 0, 'M': 0, 'A': 0, 'N': 0}
    
    # 질문과 답볍의 수
    n = len(choices)
    
    # 질문 별로 점수를 책정하여 딕셔너리에 저장하기
    for i in range(n):
        if choices[i] <= 4:
            personality[survey[i][0]] += (4 - choices[i])
        else:
            personality[survey[i][1]] += (choices[i] - 4)
    
    # 키를 슬라이싱 하기 위해서 리스트로 변환
    person_key = list(personality.keys())
    
    # 리스트를 2씩 보면서 i 와 i+1 비교 후 큰쪽 Answer에 넣기
    for i in range(0, len(person_key),2):
        if personality[person_key[i]] >= personality[person_key[i+1]]:
            answer += person_key[i]
        else:
            answer += person_key[i+1]
    return answer