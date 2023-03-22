import sys

input = sys.stdin.readline
word = [[0] * 15 for i in range(5)]
for i in range(5):
    w = list(input().rstrip())
    w_len = len(w)
    for j in range(w_len):
        word[i][j] = w[j]
for i in range(15):
    for j in range(5):
        if word[j][i] == 0:
            continue
        else:
            print(word[j][i], end='')