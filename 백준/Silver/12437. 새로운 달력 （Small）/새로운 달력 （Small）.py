t = int(input())
    
for i in range(t):
    y, m, w = map(int, input().split())
    
    cnt, result = 0, 0
    
    for _ in range(y):
        if (m + cnt) % w == 0:
            result += (m + cnt) // w
            
        else:
            result += ((m + cnt) // w) + 1
            cnt = (m + cnt) % w
            
    print(f'Case #{i + 1}: {result}')