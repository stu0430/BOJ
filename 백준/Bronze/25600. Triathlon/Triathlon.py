n = int(input())
result = 0

for _ in range(n):
    a, d, g = map(int, input().split())
    
    score = a * (d + g)
    
    if a == d + g:
        score *= 2
        
    if score > result:
        result = score
        
print(result)