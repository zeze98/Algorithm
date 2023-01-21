def hanoi_t(n, start, end):
    if n == 1:
        print(start, end)
        return
    hanoi_t(n-1, start, 6-start-end)
    print(start, end)
    hanoi_t(n-1, 6-start-end,end)

n = int(input())
print(2**n-1)
hanoi_t(n, 1, 3)