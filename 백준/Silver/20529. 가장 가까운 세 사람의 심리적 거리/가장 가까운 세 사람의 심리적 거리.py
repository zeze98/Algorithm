import sys
import itertools

input = sys.stdin.readline

t = int(input()) # 테스트 케이스의 수

# 차이 점수 구하는 함수
def find_diff(arr):
    score = 0
    a = list(arr[0])
    b = list(arr[1])
    c = list(arr[2])
    for i in range(4):
        if a[i] != b[i]:
            score += 1
        if a[i] != c[i]:
            score += 1
        if c[i] != b[i]:
            score += 1
    
    return score


for i in range(t):
    n = int(input()) # 각 테스트 케이스에서 학생의 수
    mbti = list(map(str, input().split()))
    if n > 32:
        print(0)
    else:
        all_diff = []
        for i in itertools.combinations(mbti, 3):
            all_diff.append(find_diff(i))
        print(min(all_diff))
        