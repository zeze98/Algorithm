a, b, c = map(int, input().split())
bp = 0

if b >= c:
    bp = -1
else:
    bp = a//(c-b) + 1
print(bp)