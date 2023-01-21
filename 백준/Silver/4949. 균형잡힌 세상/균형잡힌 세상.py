import sys

input = sys.stdin.readline

while True:
    s = input().rstrip()
    if s == '.':
        break

    t = True

    check = []
    for i in s:
        if i == '(' or i == '[':
            check.append(i)
        elif i == ')':
            if not check or check[-1] == '[':
                t = False
                break
            elif check[-1] == '(':
                check.pop()
        elif i == ']':
            if not check or check[-1] == '(':
                t = False
                break
            elif check[-1] == '[':
                check.pop()
    if t == True and not check:
        print('yes')
    else:
        print('no')