n = int(input())

for _ in range(n):
    score = 0
    
    name = input().replace(" ", "")
    
    for i in name:
        score += ord(i) - 64
    
    print('PERFECT LIFE' if score == 100 else score)