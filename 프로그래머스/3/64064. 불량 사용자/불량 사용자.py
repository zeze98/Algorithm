from itertools import permutations


def check(name, banned_id):
    for i in range(len(banned_id)):
        if len(name[i]) != len(banned_id[i]):
            return False
        for j in range(len(name[i])):
            if banned_id[i][j] != '*' and banned_id[i][j] != name[i][j]:
                return False
    return True


def solution(user_id, banned_id):
    answer = []
    user_list = list(permutations(user_id, len(banned_id)))
    for name in user_list:
        if not check(name, banned_id):
            continue
        else:
            result = set(name)
            if result not in answer:
                answer.append(result)

    return len(answer)