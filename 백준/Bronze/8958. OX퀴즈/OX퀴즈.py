import sys
t = int(input())
for i in range(t):
    score = 0
    quiz = list(sys.stdin.readline().rstrip().split('X'))
    for j in quiz:
        for k in range(len(j)):
            score += (k+1)
    print(score)