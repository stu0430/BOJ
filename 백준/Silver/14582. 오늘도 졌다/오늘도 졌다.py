geminis = list(map(int,input().split()))
startlink = list(map(int,input().split()))
gem_score = 0
str_score = 0
winning = False
for i in range(9):
    gem_score += geminis[i]
    if gem_score > str_score:
        winning = True
    str_score += startlink[i]
if str_score > gem_score and winning == True:
    print('Yes')
else:
    print('No')