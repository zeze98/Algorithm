import sys

input = sys.stdin.readline()

d = list(map(str,input.strip()))
anwer = []

for i in range(len(d)):
    if d[i] == 'A' or d[i] == 'B' or d[i]=='C':
        anwer.append(3)
    elif d[i] == 'D' or d[i] == 'E' or d[i] == 'F':
        anwer.append(4)
    elif d[i] == 'G' or d[i] == 'H' or d[i] == 'I':
        anwer.append(5)
    elif d[i] == 'J'or d[i] == 'K' or d[i] == 'L':
        anwer.append(6)
    elif d[i] == 'M' or d[i] == 'N' or d[i] == 'O':
        anwer.append(7)
    elif d[i] == 'P' or d[i] == 'Q' or d[i] == 'R' or d[i] == 'S':
        anwer.append(8)
    elif d[i] == 'T' or d[i] == 'U' or d[i] == 'V':
        anwer.append(9)
    elif d[i] == 'W' or d[i] == 'X' or d[i] == 'Y' or d[i] == 'Z':
        anwer.append(10)

print(sum(anwer))