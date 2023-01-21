import sys

input = sys.stdin.readline

T = int(input())
words = []
for _ in range(T):
    words.append(input().rstrip())

for i in words:
    print(i[0]+i[-1])