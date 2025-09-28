n = int(input())

result = n

for i in range(2, n):
    v = (n // i) - (i - 1)
    
    if v < 1:
        break
    
    result += v

print(result)