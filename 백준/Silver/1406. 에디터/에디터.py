import sys
input = sys.stdin.readline

word = list(input().rstrip())
ans = []

for i in range(int(input())):
    order = input().rstrip()
    if order[0] == 'L':
        if word:
            ans.append(word.pop())
        
    elif order[0] == 'D':
        if ans:
            word.append(ans.pop())
            
    elif order[0] == 'B':
        if word:
            word.pop()
    else:
        word.append(order[-1])

word.extend(reversed(ans))
print(''.join(word))