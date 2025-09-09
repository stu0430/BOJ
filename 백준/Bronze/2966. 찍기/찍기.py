p = ['ABC', 'BABC', 'CCAABB']
score = [0, 0, 0]

n = int(input())
answer = input()

for i in range(n):
    if p[0][i % 3] == answer[i]:
        score[0] += 1
    
    if p[1][i % 4] == answer[i]:
        score[1] += 1
    
    if p[2][i % 6] == answer[i]:
        score[2] += 1

print(max(score))

name = ['Adrian', 'Bruno', 'Goran']

for i in range(3):
    if score[i] == max(score):
        print(name[i])