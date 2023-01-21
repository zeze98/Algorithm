n = int(input())
score = 0
o = 1
for i in range(n):
    ans = input()
    ans = list(ans)
    for j in range(len(ans)):
        if ans[j] == 'O':
            score += o
            o += 1
        else:
            o = 1
    print(score)
    score = 0
    o = 1