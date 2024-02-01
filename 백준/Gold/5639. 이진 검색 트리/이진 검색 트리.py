import sys

input = sys.stdin.readline
sys.setrecursionlimit(10**9)

answer = []

while True:
    try:
        n = int(input())
        answer.append(n)
    except:
        break


def check(ans):
    if len(ans) == 0:
        return

    temp_left, temp_right = [], []
    mid = ans[0]

    for i in range(1, len(ans)):
        if ans[i] > mid:
            temp_left = ans[1:i]
            temp_right = ans[i:]
            break
    else:
        temp_left = ans[1:]

    check(temp_left)
    check(temp_right)
    print(mid)


check(answer)
