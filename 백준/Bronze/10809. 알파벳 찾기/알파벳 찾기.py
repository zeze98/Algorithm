word = list(map(str, input()))
index = 0
for i in range(97, 123):
    for j in range(1, len(word)+1):
        if chr(i) == word[j-1]:
            index = j
            break
    if index < len(word)+1:
        print(index-1, end=' ')
        index = 0
    elif index == 0:
        print(-1, end=' ')