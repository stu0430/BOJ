k = int(input())

for _ in range(k):
    p, m = map(int, input().split())

    d = [0] * (m + 1)
    result = 0  
    
    for _ in range(p):
        n = int(input())
    
        if d[n] == 0:
            d[n] = 1

        else:
            result += 1
            
    print(result)