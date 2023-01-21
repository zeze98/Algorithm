A = int(input())
B = int(input())
C = int(input())
n = str(A * B * C)
num_count = list()
for i in range(10):
    num_count.append(n.count(str(i)))
for i in range(10):
    print(num_count[i])