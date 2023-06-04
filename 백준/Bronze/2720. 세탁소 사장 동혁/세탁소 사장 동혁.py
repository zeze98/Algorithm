import sys
input = sys.stdin.readline

t = int(input())

def solution(c):
    change = [25,10,5,1]
    ans = []
    for i in change:
        ans.append(c//i)
        c = c % i
    return ans

for i in range(t):
    c = int(input())
    print(*solution(c))