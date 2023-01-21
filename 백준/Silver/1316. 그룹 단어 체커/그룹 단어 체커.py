n = int(input())
e = 0
for i in range(n):
    w = input()
    for j in range(len(w)-1):
        if w[j] == w[j+1]:
            pass
        elif w[j] in w[j+1:]:
            e += 1
            break

print(n-e)