import sys

input = sys.stdin.readline()
n = list(map(int,input.split()))
n.sort(reverse=True)
print(n[1])