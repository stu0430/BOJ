import sys
scores = []
for i in range(5):
    score = int(sys.stdin.readline())
    if score >= 40:
        pass
    elif score <= 40:
        score = 40
    scores.append(score)
print(sum(scores)//5)