def solution(arr):
    answer = []
    for i in range(len(arr)):
        if len(answer) == 0:
            answer.append(arr[i])
        elif answer:
            if answer[-1] == arr[i]:
                answer.pop()
            else:
                answer.append(arr[i])
    if not answer:
        return [-1]
    return answer