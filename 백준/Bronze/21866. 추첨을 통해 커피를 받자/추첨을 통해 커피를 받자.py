problems = [100, 100, 200, 200, 300, 300, 400, 400, 500]

score = list(map(int, input().split()))
total, hacker = 0, 0

for i in range(9):
    if score[i] > problems[i]:
        hacker = 1
        
    total += score[i]
    
if hacker:
    print('hacker')
    
else:
    print('draw' if total >= 100 else 'none')