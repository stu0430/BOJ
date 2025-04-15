t = int(input())

for _ in range(t):
    n = int(input())
    
    if n % 2:
        print(0)
        
    else:
        n //= 2
        print(2 ** n)