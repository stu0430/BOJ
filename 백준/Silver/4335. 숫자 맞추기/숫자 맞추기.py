while True:
    minl = 1
    maxl = 10
    
    while True:
        n = int(input())
        
        if n == 0:
            break
        
        result = input()
        
        if result == 'right on':
            if n >= minl and n <= maxl:
                result = 'Stan may be honest'
                
            else:
                result = 'Stan is dishonest'
                
            break
        
        elif result == 'too high':
            maxl = min(maxl, n - 1)
            
        elif result == 'too low':
            minl = max(minl, n + 1)
            
    if n == 0:
        break
    
    print(result)