while True:
    a = int(input())
    
    if a == 0:
        break
    
    visited = [False] * 10000
    result = 0
    
    while not visited[a]:
        result += 1
        visited[a] = True
        
        a *= a
        a %= 1000000
        a //= 100
    
    print(result)