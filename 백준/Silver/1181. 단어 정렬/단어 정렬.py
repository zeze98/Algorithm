import sys

N = int(sys.stdin.readline())
word = []
for i in range(N):
    word.append(input())
word = list(set(word))
word.sort()
word.sort(key=lambda x : len(x))
n = len(word)
for j in range(n):
    print(word[j])