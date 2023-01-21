n = int(input())

for i in range(n):
    s = list(map(int, input().split()))
    avg = sum(s[1:])/s[0]
    ns = 0
    for j in range(s[0]):
        if s[j+1] > avg:
            ns += 1
    print('{:.3f}%'.format(round(ns/s[0]*100, 3)))