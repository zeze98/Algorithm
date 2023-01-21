n = []
for i in range(10):
    n.append(int(input()))
for i in range(10):
    n[i] = n[i] % 42
print(len(set(n)))