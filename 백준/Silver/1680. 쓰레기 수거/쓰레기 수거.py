t = int(input())

for _ in range(t):
    w, n = map(int, input().split())
    
    total = 0
    result = 0
    last_x = 0
    
    for _ in range(n):
        x_i, w_i = map(int, input().split())
        last_x = x_i
        
        if total + w_i > w:
            result += 2 * x_i
            total = w_i
            
        else:
            total += w_i
            if total == w:
                result += 2 * x_i
                total = 0
    if total:
        result += 2 * last_x
        
    print(result)