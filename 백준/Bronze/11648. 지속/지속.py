n = input()

count = 0

while len(n) > 1:
    result = 1
    
    for i in n:
        result *= int(i)
        
        
    n = str(result)
    
    count += 1
    
print(count)