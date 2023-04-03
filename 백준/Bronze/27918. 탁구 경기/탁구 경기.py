n = int(input())

d, p = 0, 0

for i in range(n):
    w = input()
    
    if w == 'P':
        p += 1
        
    else:
        d += 1
    
    if abs(p - d) >= 2:
        break
    
print(f'{d}:{p}')