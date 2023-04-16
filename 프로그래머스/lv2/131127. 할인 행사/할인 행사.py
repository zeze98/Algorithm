def solution(want, number, discount):
    answer = 0
    wish = []
    for key, value in zip(want, number):
        wish += [key]*value
    wish = sorted(wish)
    for i in range(len(discount[:-len(wish) + 1])):
        answer += int(wish == sorted(discount[i: len(wish) + i]))

    return answer