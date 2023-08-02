import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())

"""
가능한 연산 
1. 2 곱하기
2. 1을 수의 가장  오른쪽에 추가
"""

# 만들어진 모든 수들이 들어갈 공간
stack = deque()
# 시작 수 a 추가
stack.append([a])

# 연산 횟수 카운트
cnt = 0
# 만들어 졌는지 못만들었는지 확인
check = 0
# 스택에서 한번 변형이 가해진걸 temp로 받아서
# 카운트 세기
while stack:
    # 변형이 가해진 수들의 리스트
    n_list = stack.popleft()
    temp = []
    for i in n_list:
        if i == b:
            check = 1
            break
        # 2 곱하는 경우 b 보다 작을때 추가
        if i*2 <= b:
            temp.append(i*2)
        # 1을 수의 가장 오른쪾에 추가하는 경우
        if int(str(i) + '1') <= b:
            temp.append(int(str(i) + '1'))
    if len(temp) >= 1:
        stack.append(temp)
    if check == 1:
        break
    cnt += 1

if check == 0:
    print(-1)
else:
    print(cnt + 1)
