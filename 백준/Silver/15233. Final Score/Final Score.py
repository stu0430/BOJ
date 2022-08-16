import sys
a,b,g = map(int,sys.stdin.readline().split())
team_a = list(map(str, sys.stdin.readline().rstrip().split()))
team_b = list(map(str, sys.stdin.readline().rstrip().split()))
goals = list(map(str, sys.stdin.readline().rstrip().split()))
a_score = 0
b_score = 0
for i in goals:
    if i in team_a:
        a_score += 1
    elif i in team_b:
        b_score += 1
if a_score > b_score:
    print('A')
elif a_score < b_score:
    print('B')
elif a_score == b_score:
    print('TIE')