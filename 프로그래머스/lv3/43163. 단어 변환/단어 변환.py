from collections import deque


def solution(begin, target, words):
    q = deque()
    q.append([begin, 0])
    visit = [False] * len(words)

    if target not in words:
        return 0

    while q:
        word, cnt = q.popleft()
        if word == target:
            return cnt
        for i in range(len(words)):
            diff_cnt = 0
            if visit[i] == False:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        diff_cnt += 1
                if diff_cnt == 1:
                    q.append([words[i], cnt + 1])
                    visit[i] = True