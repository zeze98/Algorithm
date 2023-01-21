import sys

input = sys.stdin.readline

testcase = int(input())

for i in range(testcase):
    N, M = map(int, input().split())
    Q = list(map(int, input().split()))
    printQ = [0 for j in range(N)]
    printQ[M] = 1
    cnt = 0
    while True:
        if Q[0] == max(Q):
            cnt += 1
            if printQ[0] == 1:
                print(cnt)
                break
            else:
                del Q[0]
                del printQ[0]
        else:
            Q.append(Q[0])
            del Q[0]
            printQ.append(printQ[0])
            del printQ[0]