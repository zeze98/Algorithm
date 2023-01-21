import sys

input = sys.stdin.readline

numA, numB = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
ApB = list(set(A+B))
lenAB = len(A+B) - len(ApB)

print(len(ApB) - lenAB)