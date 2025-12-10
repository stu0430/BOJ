t = int(input())

for _ in range(t):
    a, n = map(int, input().split())
    
    result = ''
    
    while a > 0:
        tmp = a % n
        
        if tmp > 9:
            tmp = chr(55 + tmp)
            
        result = str(tmp) + result
        
        a //= n
        
    if result == result[::-1]:
        print(1)
    else:
        print(0)