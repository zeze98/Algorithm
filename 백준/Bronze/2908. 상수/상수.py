x, y = input().split()
if str(x)[::-1] >= str(y)[::-1]:
    print(str(x)[::-1])
else:
    print(str(y)[::-1])