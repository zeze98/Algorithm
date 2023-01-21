x, y, w, h = list(map(int,input().split()))
short = [x, y, w, h]
short.append(w-x)
short.append(h-y)

print(min(short))