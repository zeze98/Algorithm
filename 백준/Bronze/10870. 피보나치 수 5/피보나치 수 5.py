n = int(input())
pibon = 0
p_list = []
def pibo(n):
    for i in range(n+1):
        if i == 0:
            pibon = 0
            p_list.append(pibon)
        elif i == 1:
            pibon = 1
            p_list.append(pibon)
        elif i >= 2:
            pibon = p_list[i-2]+p_list[i-1]
            p_list.append(pibon)
    print(p_list[n])
pibo(n)