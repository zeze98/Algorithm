import sys

input = sys.stdin.readline()

w = input

for i in range(0,len(w),10):
    print(w[i:i+10])