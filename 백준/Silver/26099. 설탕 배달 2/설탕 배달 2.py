n = int(input())

for i in range(5):
    x = n - (i * 3)
    
    if x < 0:
        break
    
    if x % 5 == 0:
        print(i + (x // 5))
        exit()
        
print(-1)