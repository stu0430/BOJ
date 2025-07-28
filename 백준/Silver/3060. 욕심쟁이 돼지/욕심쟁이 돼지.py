t = int(input())

for _ in range(t):
    n = int(input())
    m = sum(list(map(int, input().split())))
    
    result = 1
    
    while n >= m:
        result += 1
        m *= 4
        
    print(result)