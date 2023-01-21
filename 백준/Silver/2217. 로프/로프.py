N = int(input())
rope = []
answer = []
for i in range(N):
    rope.append(int(input()))
rope.sort(reverse=True)
for x in range(1, N + 1):
    w = x * rope[x-1]
    answer.append(w)

print(max(answer))