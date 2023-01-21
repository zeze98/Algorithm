import math
import sys

def primenumber(x):
    for i in range(2, int(math.sqrt(x) + 1)):
        if x % i == 0:
            return False
    return True

n = sys.stdin.readline()
num = list(map(int, sys.stdin.readline().split()))
answer = 0

for i in range(int(n)):
    if num[i] == 1:
        answer += 0
    else:
        if primenumber(num[i]):
            answer += 1
print(answer)