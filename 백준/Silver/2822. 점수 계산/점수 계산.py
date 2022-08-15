score = []
score_2 = []
for i in range(8):
    a = int(input())
    score.append(a)
    score_2.append(a)
score_2.sort()
score_2 = score_2[3:]
score_idx = []
for j in score_2:
    score_idx.append(score.index(j)+1)
score_idx.sort()
print(sum(score_2))
for k in score_idx:
    print(k, end=' ')