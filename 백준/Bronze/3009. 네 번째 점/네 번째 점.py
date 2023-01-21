x = []
y = []
for _ in range(3):
    xx, yy = map(int, input().split())
    x.append(xx)
    y.append(yy)

for i in range(3):
    if x.count(x[i]) == 1:
        x1 = x[i]
    if y.count(y[i]) == 1:
        y1 = y[i]
print(x1, y1)