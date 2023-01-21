import sys

input = sys.stdin.readline

L = int(input())
s = str(input())
M = 1234567891
h = 0
for i in range(L):
   h += (ord(s[i])-96)*31**i

if h > M:
    h = h/M

print(h)