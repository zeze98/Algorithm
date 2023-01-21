import sys

input = sys.stdin.readline

n, k = list(map(int, input().split()))
A = list(map(int, input().split()))
ans = -1

def merge_sort(A, i, j):
    if i < j:
        m = (i+j)//2
        merge_sort(A, i, m)
        merge_sort(A, m+1, j)
        merge(A, i, m+1, j)

def merge(A, i, m, j):
    global k
    global ans
    p = i
    q = m
    r = 0
    temp = [0] * (j-i+1)
    while p < m and q <= j:
        k -= 1
        if A[p] > A[q]:
            temp[r] = A[q]
            q += 1
        else:
            temp[r] = A[p]
            p += 1
        if k == 0:
            ans = temp[r]
        r += 1

    while p < m:
        temp[r] = A[p]
        k -= 1
        if k == 0:
            ans = temp[r]
        p += 1
        r += 1

    while q <= j:
        temp[r] = A[q]
        k -= 1
        if k == 0:
            ans = temp[r]
        q += 1
        r += 1

    p = i
    i = 0
    while p <= j:
        A[p] = temp[i]
        p += 1
        i += 1

merge_sort(A, 0, n-1)
print(ans)