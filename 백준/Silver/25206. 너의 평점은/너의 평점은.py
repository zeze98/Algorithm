import sys

input = sys.stdin.readline

total = 0
t_score = 0
score_dic = {'A+': 4.5, 'A0': 4.0, 'B+': 3.5, 'B0': 3.0, 'C+': 2.5, 'C0': 2.0, 'D+': 1.5, 'D0': 1.0, 'F': 0}
for _ in range(20):
    name, t, s = map(str, input().split())
    if s == 'P':
        continue
    if s in score_dic.keys():
        total += float(t)
        t_score = t_score + (float(t) * score_dic[s])

print(f'{t_score / total:.6f}')