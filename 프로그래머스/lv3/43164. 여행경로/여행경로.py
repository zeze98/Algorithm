def solution(tickets):
    answer = []
    tickets_dic = {}

    for start, end in tickets:
        tickets_dic[start] = tickets_dic.get(start, []) + [end]
    for k in tickets_dic:
        tickets_dic[k].sort(reverse=True)
    stack = ['ICN']

    while len(stack) > 0:
        top = stack[-1]

        if top not in tickets_dic or len(tickets_dic[top]) == 0:
            answer.append(stack.pop())
        else:
            stack.append(tickets_dic[top][-1])
            tickets_dic[top] = tickets_dic[top][:-1]

    return answer[::-1]