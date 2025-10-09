for i in range(int(input())):
    a, b, c = sorted(map(int, input().split()))
    print(f'Case #{i + 1}: ', end='')
    
    if a + b <= c:
        print('invalid!')
        
    elif a == b == c:
        print('equilateral')
        
    elif a == b or b == c:
        print('isosceles')
        
    else:
        print('scalene')