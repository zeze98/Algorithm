import math
import sys

input = sys.stdin.readline

N = int(input())
FacN = math.factorial(N)
listN = list(str(FacN))
count_0 = 0

if len(listN) > 1:
    for i in range(len(listN)-1,0,-1):
        if listN[i] == '0':
            count_0 += 1
        else:
            count_0 = count_0
            print(count_0)
            break
else:
    print(0)