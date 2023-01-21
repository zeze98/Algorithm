def answer(N):
    hansu = 0
    for i in range(1,N+1):
        N_list = list(map(int, str(i)))
        if i < 100:
            hansu += 1
        elif N_list[0] - N_list[1] == N_list[1] - N_list[2]:
            hansu += 1
    return hansu

N = int(input())
print(answer(N))