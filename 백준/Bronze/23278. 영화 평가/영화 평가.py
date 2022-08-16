n,l,h = map(int, input().split())
score = list(map(int, input().split()))
score.sort()
score = score[l:]
if h == 0:
    pass
else: 
    score = score[:-(h)]
print(sum(score)/len(score))