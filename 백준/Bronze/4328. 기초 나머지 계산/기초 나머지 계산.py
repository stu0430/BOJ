while True:
    array = list(map(int, input().split()))
    
    if array[0] == 0:
        break
    
    b, p, m = array[0], array[1], array[2]
    
    n = int(str(p), b) % int(str(m), b)
    
    result = []
    while n >= b:
        result.append(str(n % b))
        n //= b
        
    result.append(str(n))
    
    print(int(''.join(result[::-1])))