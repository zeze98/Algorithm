N = int(input())
answer = 0

if N == 4 or N == 7:
    answer = -1
else:
    answer += N // 5
    N %= 5
    if N == 0:
        answer = answer
    elif N == 1 or N == 3:
        answer += 1
    elif N == 2 or N == 4:
        answer += 2

print(answer)
