import sys

N = int(sys.stdin.readline())
N_list = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline())
M_list = list(map(int, sys.stdin.readline().split()))

answer = {}
for i in range(N):
    answer[N_list[i]] = 0

for j in range(M):
    if M_list[j] not in answer:
        print(0, end=' ')
    else:
        print(1, end=' ')