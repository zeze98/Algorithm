import sys

input = sys.stdin.readline

def recursion(s,l,r,x):

    if l >= r:
        return print(1, x, end=' '), print()
    elif s[l] != s[r]:
        return print(0, x, end=' '), print()
    else:
        return recursion(s, l + 1, r - 1,x + 1)

def isPalindrome(s):
    return recursion(s, 0, len(s)-1, 1)

T = int(input())
S = []

for _ in range(T):
    S.append(str(input().rstrip()))

for i in range(T):
    isPalindrome(S[i])