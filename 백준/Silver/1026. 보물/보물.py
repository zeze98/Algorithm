N = int(input())
A_list = list(map(int, input().split()))
B_list = list(map(int, input().split()))
s = 0

a = sorted(A_list, reverse=True)
b = sorted(B_list)

for i in range(N):
    s = s + a[i] * b[i]

print(s)