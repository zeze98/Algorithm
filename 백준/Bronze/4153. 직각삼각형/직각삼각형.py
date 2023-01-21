import sys

tri = list(map(int,sys.stdin.readline().split()))

while tri[0] != 0:
    tri_sort = sorted(tri)
    if ((tri_sort[0]**2) + (tri_sort[1]**2) == (tri_sort[2]**2)):
        print('right')
    else:
        print('wrong')
    tri = list(map(int, sys.stdin.readline().split()))