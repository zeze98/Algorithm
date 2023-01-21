count = 0
n = list()
while count < 9:
    n.append(int(input()))
    count += 1
print(max(n))
print(n.index(max(n))+1)