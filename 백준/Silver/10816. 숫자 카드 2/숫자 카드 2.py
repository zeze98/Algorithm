import sys
from collections import Counter

input = sys.stdin.readline

N = int(input())
cardN = input().split()
M = int(input())
cardM = input().split()

c = Counter(cardN)
print(' '.join(f'{c[m]}' if m in c else '0' for m in cardM))