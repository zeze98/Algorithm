import sys

input = sys.stdin.readline

N = int(input())
cnt = 0
sixn = 666

while True:
    if '666' in str(sixn):
        cnt += 1
    if cnt == N:
        print(sixn)
        break
    sixn += 1