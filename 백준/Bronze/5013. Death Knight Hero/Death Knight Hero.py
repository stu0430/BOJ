n = int(input())
won = 0
    
for _ in range(n):
    k = list(input())
    
    flag = True
    for i in range(len(k) - 1):
        if k[i] == 'C' and k[i + 1] == 'D':
            flag = False
            break
        
    if flag:    
        won += 1
            
print(won)