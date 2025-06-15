while True:
    n = input()
    
    if n == '0':
        break
    
    while len(n) > 1:
        result = 1
        
        print(n, end=' ')
        
        for i in n:
            result *= int(i)
            
        n = str(result)
        
    print(n)