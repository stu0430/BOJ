n = int(input())

result = 0

k = 1
while n > 0:
    n -= k
    
    if n <= k:
        k = 0
    
    result += 1
    k += 1
    
print(result)