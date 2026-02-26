n = int(input())

if n == 0:
    print(0)
    
elif n == 1:
    print(4)
    
else:
    i = 0
    while i * i < n:
        i += 1
        
    if (i - 1) * i > n:
        print((i - 2 + i - 1) * 2)
        
    else:
        print((i - 1) * 4)