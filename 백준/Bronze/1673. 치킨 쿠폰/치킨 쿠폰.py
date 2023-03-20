while True:
    try:
        n, k = map(int, input().split())
        
        count = n
        
        while n >= k:
            count += n // k
            n = n // k + n % k
            
        print(count)
        
    except:
        break