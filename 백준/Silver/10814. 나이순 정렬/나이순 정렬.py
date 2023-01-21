import sys

n = int(sys.stdin.readline())
member = []

for i in range(n):
    member.append(list(sys.stdin.readline().split()))
member.sort(key=lambda x: int(x[0]))
for j in range(n):
    print(member[j][0],member[j][1])