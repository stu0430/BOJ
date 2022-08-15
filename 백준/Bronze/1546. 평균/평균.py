n = int(input())
score = list(map(int, input().split()))
m = max(score)
new_score = []
X = 0
for i in score:
    new_score.append(i/m*100)
for j in new_score:
    X += j
print(X/len(new_score))