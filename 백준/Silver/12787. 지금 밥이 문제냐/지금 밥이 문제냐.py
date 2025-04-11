t = int(input())

for _ in range(t):
    m, n = input().split()
    
    if m == '1':
        result = ''
        ipv8 = list(map(int, n.split('.')))
        
        for i in ipv8:
            result += bin(i)[2:].zfill(8)
            
        print(int(result, 2))
    
    elif m == '2':
        result = ''
        u_int = str(bin(int(n))[2:]).zfill(64)
        
        for i in range(8):
            result += str(int(u_int[i * 8:(i + 1) * 8], 2))
            
            if i != 7:
                result += '.'
                
        print(result)