import sys

a, b = sys.stdin.readline().split()
mia = a.replace('6', '5')
mib = b.replace('6', '5')
MAA = a.replace('5', '6')
MAB = b.replace('5', '6')
Min = int(mia) + int(mib)
Max = int(MAA) + int(MAB)
print(Min, Max)