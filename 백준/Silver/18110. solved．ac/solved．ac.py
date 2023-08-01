import sys

input = sys.stdin.readline


def rnd(num):
    if (num - int(num)) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(input())
if n == 0:
    answer = 0
else:
    opinion = [int(input()) for _ in range(n)]
    cut = rnd(n * 0.15)
    cut_opinion = sorted(opinion)[cut: n - cut]
    answer = rnd(sum(cut_opinion) / len(cut_opinion))
print(answer)
