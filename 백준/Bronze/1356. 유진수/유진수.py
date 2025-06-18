n = list(map(int, input()))

if len(n) == 1:
    print('NO')
    
else:
    a, b = 1, 1

    for i in range(len(n) - 1):
        a, b = 1, 1

        for j in range(i + 1):
            a *= n[j]

        for k in range(i + 1, len(n)):
            b *= n[k]

        if a == b:
            break
    
    if a == b:
        print('YES')
        
    else:
        print('NO')