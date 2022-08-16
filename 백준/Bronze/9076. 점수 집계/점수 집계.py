import sys
t = int(sys.stdin.readline())
for i in range(t):
    score = list(map(int, sys.stdin.readline().split()))
    score.sort()
    del score[0]
    del score[-1]
    high_score = max(score)
    low_score = min(score)
    if high_score - low_score >= 4:
        print('KIN')
    else:
        print(sum(score))