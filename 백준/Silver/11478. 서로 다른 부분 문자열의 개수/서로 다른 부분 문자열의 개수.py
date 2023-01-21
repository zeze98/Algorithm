import sys

input = sys.stdin.readline

s = input().rstrip()
lists = []
for i in range(1,len(s)+1):
    for j in range(len(s)):
        lst = s[j:j+i]
        lists.append(lst)

S = list(set(lists))
print(len(S))