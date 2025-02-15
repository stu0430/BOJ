n = int(input())

result, a = 1, 1

for i in range(n):
    if i % 2 != 0:
        a += 1
        
    result += a
    
print(result)