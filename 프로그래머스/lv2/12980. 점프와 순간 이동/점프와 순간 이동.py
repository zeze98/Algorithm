def solution(n):
    ans = 0
    now = n
    while now != 0:
        if now % 2 == 0:
            now = now // 2
        else:
            ans += 1
            now -=1
    return ans
