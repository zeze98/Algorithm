def solution(my_string):
    answer = ''
    delete_list = ['a','i', 'o', 'e', 'u']
    for i in my_string:
        if i not in delete_list:
            answer += i
    return answer