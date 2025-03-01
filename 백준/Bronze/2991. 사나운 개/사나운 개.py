a, b, c, d = map(int, input().split())
p, m, n = map(int, input().split())

for i in [p, m, n]:
    result = 0
    
    if 0 < i % (a + b) <= a:
        result += 1
        
    if 0 < i % (c + d) <= c:
        result += 1
        
    print(result)